from django.conf.urls import patterns, include, url
from django.conf import settings
import cart.views
import orders.views
import customers.views

urlpatterns = patterns('',
    #url(r'^$', 'orders.views.checkout', name='checkout'),
    url(r'add/$', 'customers.views.add_recipient', name='add_recipient'),
    #url(r'^rebuild/(?P<cart_id>[-\w]+)/$', 'cart.views.cart_rebuilder', name='cart_rebuilder'),
    #url(r'^add/(?P<slug>[-\w]+)/$', 'cart.views.add_to_cart', name='add_to_cart'),
    #url(r'^increment/(?P<slug>[-\w]+)/$', 'cart.views.increment_cart', name='increment_cart'),
    #url(r'^decrement/(?P<slug>[-\w]+)/$', 'cart.views.decrement_cart', name='decrement_cart'),
    #url(r'^update/(?P<slug>[-\w]+)/$', 'cart.views.update_cart', name='update_cart'),
    #url(r'^remove/(?P<slug>[-\w]+)/$', 'cart.views.remove_from_cart', name='remove_from_cart'),
    #url(r'^delete$', 'cart.views.delete', name='cart_empty'),
    #url(r'^checkout$', 'orders.views.czechout', name='czechout'),
    #url(r'^pay/(?P<order_id>[-\w]+)/$', orders.views.payout, name='payout'),
    #url(r'^result/(?P<order_id>[-\w]+)/$', orders.views.result, name='result'),
)
