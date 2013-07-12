from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'post.views.home', name='home'),
    # url(r'^post/', include('post.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'signups.views.connect', name='connect'),
    url(r'^signups/success/$', 'signups.views.success', name='success'),
    url(r'^signups/messages.html$', TemplateView.as_view(template_name='signups/messages.html')),
   
    
)

urlpatterns += staticfiles_urlpatterns()

handler404 = 'post.views.custom404'