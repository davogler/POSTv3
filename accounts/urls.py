from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from accounts.views import DashTemplateView


import accounts.views


urlpatterns = [

    url(r'^$', login_required(DashTemplateView.as_view(template_name="accounts/dashboard.html")), name="dashboard"),
    url(r'^logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^password_reset/', include('password_reset.urls')),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),



]
