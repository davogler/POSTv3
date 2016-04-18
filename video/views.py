from django.shortcuts import render
from video.models import VideoPost
import datetime
import itertools
from django.views.generic import ListView, DetailView
from sponsors.models import Advert


def video_sort(request):
    '''checks if the user is authenticated-if so, make a queryset consisting of unpublished entries and published entries.  If not authenticated, the queryset is just published entries'''
    pubset = VideoPost.published.exclude(timestamp__gte=datetime.datetime.now())
    if request.user.is_authenticated():
        unpubset = VideoPost.draft.exclude(timestamp__gte=datetime.datetime.now())
    else:
        unpubset = VideoPost.published.exclude(timestamp__gte=datetime.datetime.now())
    queryset = (pubset | unpubset)
    queryset = queryset.exclude(timestamp__gte=datetime.datetime.now())
    return queryset


def video_list(request):
    post_videos = VideoPost.published.filter(type=1)
    community_videos = VideoPost.published.filter(type=2)
    try:
        ad1 = Advert.objects.filter(is_active=True).get(position=1)
    except:
        ad1 = None
    try:
        ad2 = Advert.objects.filter(is_active=True).get(position=2)
    except:
        ad2 = None

    context = {"post_videos": post_videos, "community_videos": community_videos, "ad1":ad1, "ad2":ad2}
    template = "video/video_list.html"
    return render(request, template, context)


class VideoDetail(DetailView):

    '''The individual article view- permalink location.  Uses dispatch to apply a sorted queryset, depending on authentication state of requesting user.'''

    allow_empty = True
    allow_future = False

    model = VideoPost
    context_object_name = 'video'

    def get_template_names(self):
        '''if the article has template name set, use that template.  otherwise, go standard'''
        return [(self.get_object().template_name), 'video/video_detail.html']

    def dispatch(self, request, *args, **kwargs):
        self.queryset = video_sort(request)

        return super(VideoDetail, self).dispatch(request, *args, **kwargs)

    def get_next(self):
        next = VideoPost.objects.filter(id__gt=self.id)
        if next:
            return next[0]
        return False

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VideoDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        next = VideoPost.objects.filter(pub_date__gt=self.get_object().pub_date).order_by('pub_date') 
        prev = VideoPost.objects.filter(pub_date__lt=self.get_object().pub_date).order_by('-pub_date') 

        ttl = itertools.islice((itertools.chain(next, prev)), 4)
        # qt = self.get_object().igtag_set.all
        # duh = InstaPost.objects.filter(tag=qt).filter(active="True")
        # igtags = IGTag.objects.filter(articles=self.get_object())
        # realtime_igtags = IGTag.objects.filter(articles=self.get_object()).exclude(ig_id__isnull=True).exclude(ig_id__exact='')
        # inactive_igtags = IGTag.objects.filter(articles=self.get_object()).filter(Q(ig_id__exact='') | Q(ig_id__isnull=True))


        context['ttl'] = ttl
        return context
