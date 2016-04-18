from django.conf.urls import patterns, include, url
from django.conf import settings
import cart.views
import orders.views


urlpatterns = patterns('',
    url(r'^$', 'orders.views.checkout', name='checkout'),
    url(r'^list/$', 'orders.views.order_list', name='order_list'),
    url(r'^list/(?P<order_id>[-\w]+)/$', 'orders.views.order_detail', name='order_detail'),
    url(r'^record/list/$', 'orders.views.record_list', name='record_list'),
    url(r'^record/add/(?P<order_id>[-\w]+)/$', 'orders.views.order_record', name='order_record'),
    url(r'^record/issue/(?P<issue>[-\w]+)/$', 'orders.views.record_by_issue', name='record_by_issue'),
    url(r'^result/(?P<order_id>[-\w]+)/$', orders.views.result, name='result'),
    url(r'^email/(?P<order_id>[-\w]+)/$', orders.views.email, name='email'),
    url(r'^email_preview/(?P<order_id>[-\w]+)/$', orders.views.email_preview, name='email_preview'),
)
