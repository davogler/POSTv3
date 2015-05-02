from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.db.models import Q
from articles.models import Article, Issue
from insta.models import InstaPost, IGTag
import datetime
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator
from django.http import Http404
from django.template import RequestContext
from django.template import loader, Context


def entry_sort(request):
    '''checks if the user is authenticated-if so, make a queryset consisting of unpublished entries and published entries.  If not authenticated, the queryset is just published entries'''
    pubset = Article.published.exclude(pub_date__gte=datetime.datetime.now())
    if request.user.is_authenticated():
        unpubset = Article.draft.exclude(pub_date__gte=datetime.datetime.now())
    else:
        unpubset = Article.published.exclude(pub_date__gte=datetime.datetime.now())
    queryset = (pubset | unpubset)
    queryset = queryset.exclude(pub_date__gte=datetime.datetime.now())
    return queryset


def issue_sort(request):
    '''checks if the user is authenticated-if so, make a queryset consisting of unpublished entries and published entries.  If not authenticated, the queryset is just published entries'''
    pubset = Issue.published.exclude(pub_date__gte=datetime.datetime.now())
    if request.user.is_authenticated():
        unpubset = Issue.draft.exclude(pub_date__gte=datetime.datetime.now())
    else:
        unpubset = Issue.published.exclude(pub_date__gte=datetime.datetime.now())
    queryset = (pubset | unpubset)
    queryset = queryset.exclude(pub_date__gte=datetime.datetime.now())
    return queryset


class ArticleDetail(DetailView):

    '''The individual article view- permalink location.  Uses dispatch to apply a sorted queryset, depending on authentication state of requesting user.'''

    allow_empty = True
    allow_future = False

    model = Article
    context_object_name = 'article'

    def get_template_names(self):
        '''if the article has template name set, use that template.  otherwise, go standard'''
        return [(self.get_object().template_name), 'articles/article_detail.html']

    def dispatch(self, request, *args, **kwargs):
        self.queryset = entry_sort(request)

        return super(ArticleDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        
        qt = self.get_object().igtag_set.all
        duh = InstaPost.objects.filter(tag=qt).filter(active="True")
        igtags = IGTag.objects.filter(articles=self.get_object())
        realtime_igtags = IGTag.objects.filter(articles=self.get_object()).exclude(ig_id__isnull=True).exclude(ig_id__exact='')
        inactive_igtags = IGTag.objects.filter(articles=self.get_object()).filter(Q(ig_id__exact='') | Q(ig_id__isnull=True))


        
        
       
        context['realtime_igtags'] = realtime_igtags
        context['inactive_igtags'] = inactive_igtags

        
        context['igtags'] = igtags
        context['media_list'] = duh
        return context


class ArticleFeatured(DetailView):

    '''The featured article on the home page'''

    model = Article
    context_object_name = 'article'

    def get_object(self):
        qs = Article.published.filter(featured=True).latest('pub_date')
        pk = qs.id
        return get_object_or_404(Article, pk=pk)

    def get_template_names(self):
        '''if the article has template name set, use that template.  otherwise, go standard'''
        return [(self.get_object().template_name), 'articles/article_detail.html']


class ArticleList(ListView):

    '''A List view of published articles'''
    template_name = 'article_list.html'
    allow_empty = True
    allow_future = False

    model = Article
    context_object_name = 'article'
    queryset = Article.published.all()


class ArticlePreviewList(ListView):

    '''A List view of published articles- authenticated required via URL'''
    template_name = 'articles/unpublished.html'
    allow_empty = True
    allow_future = False

    model = Article
    context_object_name = 'article'
    queryset = Article.draft.all()


class CustomFeedGenerator(Rss201rev2Feed):

    def add_item_elements(self, handler, item):
        super(CustomFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement(u"image", item['image'])


class ArticleFeed(Feed):
    title = "Post Magazine Featured Articles"
    description_template = 'feeds/latest_title.html'
    link = "/"
    description = "Updates as new articles are published"
    description_template = 'feeds/latest_description.html'
    image_template = 'feeds/latest_image.html'
    item_copyright = 'Copyright (c) Post Magazine'
    feed_type = CustomFeedGenerator

    def items(self):
        return Article.published.all().order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.pub_date

    def item_author_name(self, item):
        return item.get_author()

    def item_description(self, item):
        return item.intro

    def item_extra_kwargs(self, obj):
        """
        Returns an extra keyword arguments dictionary that is used with
        the `add_item` call of the feed generator.
        Add the 'content' field of the 'Entry' item, to be used by the custom feed generator.
        """
        return {'image': obj.get_feednail() if obj.hero.url else "",
                }


class IssueFeatured(DetailView):

    '''The featured issue on the home page'''

    model = Issue
    context_object_name = 'Issue'

    def get_object(self):
        qs = Issue.published.latest('pub_date')
        pk = qs.id
        return get_object_or_404(Issue, pk=pk)

    def get_template_names(self):
        '''if the issue has template name set, use that template.  otherwise, go standard'''
        return [(self.get_object().template_name), 'articles/issue_detail.html']


class IssueList(ListView):

    '''A List view of Issues'''
    template_name = 'articles/issue_master_list.html'
    allow_empty = True
    allow_future = False

    model = Issue
    context_object_name = 'Issue'
    queryset = Issue.published.all()


class IssueDetail(DetailView):

    '''The individual article view- permalink location.  Uses dispatch to apply a sorted queryset, depending on authentication state of requesting user.'''

    allow_empty = True
    allow_future = False

    model = Issue
    context_object_name = 'Issue'
    slug_field = 'slug'

    def get_template_names(self):
        '''if the article has template name set, use that template.  otherwise, go standard'''
        return [(self.get_object().template_name), 'articles/issue_detail.html']

    def dispatch(self, request, *args, **kwargs):
        self.queryset = issue_sort(request)

        return super(IssueDetail, self).dispatch(request, *args, **kwargs)
