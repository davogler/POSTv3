from django.conf.urls import *
from django.conf import settings
from filebrowser.sites import site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from articles.models import Article
from articles.views import ArticleDetail, ArticleList, ArticleFeatured

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'post.views.home', name='home'),
    # url(r'^post/', include('post.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    # url(r'^$', 'signups.views.connect', name='connect'),
    url(r'^$', ArticleFeatured.as_view(), name='article_detail'),
    url(r'^archive/$', ArticleList.as_view(), name='article_list'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='article_detail'),
    url(r'^signups/success/$', 'signups.views.success', name='success'),
    url(r'^signups/messages.html$', TemplateView.as_view(template_name='signups/messages.html')),
    url(r'^subscribers/get/$', 'subscribers.views.get_subscriber', name='subscribe'),
   
    
)

urlpatterns += staticfiles_urlpatterns()

handler404 = 'post.views.custom404'