from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from articles.models import Article
import datetime
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator
from django.http import Http404
from django.template import RequestContext


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

class ArticleDetail(DetailView):
    '''The individual article view- permalink location.  Uses dispatch to apply a sorted queryset, depending on authentication state of requesting user.'''
    template_name = 'article_detail.html'
    allow_empty = True
    allow_future = False
    
    model = Article
    context_object_name = 'article'
   
    
    def dispatch(self, request, *args, **kwargs):
        self.queryset = entry_sort(request)
        
        return super(ArticleDetail, self).dispatch(request, *args, **kwargs)
    
    
            
class ArticleFeatured(DetailView):
    '''The featured article on the home page'''
    template_name = 'article_detail.html'

    
    model = Article
    context_object_name = 'article'
    
    
    def get_object(self):
        qs = Article.published.filter(featured=True).latest('pub_date')
        pk = qs.id
        return get_object_or_404(Article, pk=pk)
     
    
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
    template_name = 'article_list.html'
    allow_empty = True
    allow_future = False
    
    model = Article
    context_object_name = 'article'
    queryset = Article.draft.all()
    
            
