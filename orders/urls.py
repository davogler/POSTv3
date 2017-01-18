from django.conf.urls import patterns, include, url
from django.conf import settings
import cart.views
import orders.views


urlpatterns = patterns('',
    url(r'^$', 'orders.views.checkout', name='checkout'),
    url(r'^saved/$', 'orders.views.checkout_saved_cc', name='checkout_saved_cc'),
    url(r'^toggle_renew/(?P<item_id>[-\w]+)/$', 'orders.views.toggle_renew', name='toggle_renew'),
    url(r'^renewals/$', 'orders.views.renewals_get', name='renewals_get'),
    url(r'^renewals/(?P<issue>(\d+))/$', 'orders.views.renewals', name='renewals'),
    url(r'^list/$', 'orders.views.order_list', name='order_list'),
    url(r'^list/(?P<order_id>[-\w]+)/$', 'orders.views.order_detail', name='order_detail'),
    url(r'^records/$', 'orders.views.records_get', name='records_get'),
    url(r'^records/(?P<issue>(\d+))/$', 'orders.views.records', name='records'),
    url(r'^record/add/(?P<order_id>[-\w]+)/$', 'orders.views.order_record', name='order_record'),
    url(r'^record/issue/(?P<issue>[-\w]+)/$', 'orders.views.record_by_issue', name='record_by_issue'),
    url(r'^result/(?P<order_id>[-\w]+)/$', orders.views.result, name='result'),
    url(r'^email/(?P<order_id>[-\w]+)/$', orders.views.email, name='email'),
    url(r'^email_preview/(?P<order_id>[-\w]+)/$', orders.views.email_preview, name='email_preview'),
)
