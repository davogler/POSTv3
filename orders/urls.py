from django.conf.urls import patterns, include, url
from django.conf import settings
import cart.views
import orders.views


urlpatterns = patterns('',
   url(r'^$', 'orders.views.checkout', name='checkout'),
   url(r'^auto_renewal/$', 'orders.views.checkout_auto_renewal', name='checkout_auto_renewal'),
   url(r'^saved/$', 'orders.views.checkout_saved_cc', name='checkout_saved_cc'),
   url(r'^add_card/$', 'orders.views.add_credit_card', name='add_card'),
   url(r'^accept_coupon/$', 'orders.views.accept_coupon', name='accept_coupon'),
   url(r'^toggle_renew/(?P<item_id>[-\w]+)/$', 'orders.views.toggle_renew', name='toggle_renew'),
   url(r'^renewals/$', 'orders.views.renewals_get', name='renewals_get'),
   url(r'^renewals/(?P<issue>(\d+))/$', 'orders.views.renewals', name='renewals'),
   url(r'^list/$', 'orders.views.order_list', name='order_list'),
   url(r'^list/(?P<order_id>[-\w]+)/$', 'orders.views.order_detail', name='order_detail'),
   url(r'^comps/export/(?P<type>[-\w]+)/$', 'orders.views.comps_export', name='comps_export'),
   url(r'^records/$', 'orders.views.records_get', name='records_get'),
   url(r'^records/export/(?P<issue>(\d+))/$', 'orders.views.records_export', name='records_export'),
   url(r'^records/(?P<issue>(\d+))/$', 'orders.views.records', name='records'),
   url(r'^record/add/(?P<order_id>[-\w]+)/$', 'orders.views.order_record', name='order_record'),
   url(r'^record/issue/(?P<issue>[-\w]+)/$',
       'orders.views.record_by_issue', name='record_by_issue'),
   url(r'^promo_to_record/$', 'orders.views.promo_to_record', name='promo_to_record'),
   url(r'^promos/$', 'orders.views.promos', name='promos'),
   url(r'^result/(?P<order_id>[-\w]+)/$', orders.views.result, name='result'),
   url(r'^email/(?P<order_id>[-\w]+)/$', orders.views.email, name='email'),
   url(r'^email_preview/(?P<order_id>[-\w]+)/$', orders.views.email_preview, name='email_preview'),
   url(r'^email_pending_renewal/(?P<record_id>[-\w]+)/$',
       orders.views.email_pending_renewal, name='email_pending_renewal'),
   url(r'^email_pending_renewal_preview/(?P<record_id>[-\w]+)/$',
       orders.views.email_pending_renewal_preview, name='email_pending_renewal_preview'),
   )
