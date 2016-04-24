from django.conf.urls import *
from django.conf import settings
from filebrowser.sites import site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, RedirectView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from articles.models import Article, Issue
from articles.views import ArticleDetail, ArticleList, ArticleFeatured, ArticlePreviewList, ArticleFeed, IssueFeatured, IssueList, IssueDetail

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
    url(r'^feed/$', ArticleFeed()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    # url(r'^$', 'signups.views.connect', name='connect'),
    #url(r'^$', ArticleFeatured.as_view(), name='article_detail'),
    url(r'^$', IssueFeatured.as_view(), name='issue_detail'),
    url(r'^articles/$', ArticleList.as_view(), name='article_list'),
    url(r'^account/', include('accounts.urls')),
    url(r'^issues/$', IssueList.as_view(), name='issue_master_list'),
    url(r'^issues/(?P<slug>[-\w]+)/$', IssueDetail.as_view(), name='issue_detail'),
    url(r'^preview/$', login_required(ArticlePreviewList.as_view()), name='article_preview_list'),
    url(r'^subscribe/$', 'signups.views.connect', name='connect'),
    url(r'^issue-four/$', RedirectView.as_view(url='/issues/4/')),
    url(r'^issue-five/$', RedirectView.as_view(url='/issues/5/')),
    url(r'^issue-6/$', RedirectView.as_view(url='/issues/6/')),
    url(r'^issue-7/$', RedirectView.as_view(url='/issues/7/')),
    #url(r'^catalog/', 'catalog.views.product_list', name='product_list'),
    url(r'^cart/', include('cart.urls')),
    url(r'^order/', include('orders.urls')),
    url(r'^customer/', include('customers.urls')),
    url(r'^instagram/', include('insta.urls')),
    url(r'^video/', include('video.urls')),
    url(r'^flip/', TemplateView.as_view(template_name='turning_test.html'), name="flip"),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='article_detail'),
    url(r'^signups/success/$', 'signups.views.success', name='success'),
    url(r'^signups/messages.html$', TemplateView.as_view(template_name='signups/messages.html')),
    url(r'^subscribers/get/$', 'subscribers.views.get_subscriber', name='subscribe'),
   
    
)

urlpatterns += staticfiles_urlpatterns()

handler404 = 'post.views.custom404'