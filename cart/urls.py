from django.conf.urls import patterns, include, url
from django.conf import settings
import cart.views
import orders.views

urlpatterns = patterns('',
    url(r'^$', 'cart.views.view_cart', name='view_cart'),
    #url(r'^rebuild/(?P<cart_id>[-\w]+)/$', 'cart.views.cart_rebuilder', name='cart_rebuilder'),
    url(r'^add/(?P<slug>[-\w]+)/$', 'cart.views.add_to_cart', name='add_to_cart'),
    url(r'^add_again/(?P<recipient_id>[-\w]+)/$', 'cart.views.add_subscribe_again_to_cart', name='add_again'),
    url(r'^renew/(?P<slug>[-\w]+)/(?P<recipient_id>[-\w]+)$', 'cart.views.add_renewal_to_cart', name='add_renewal'),
    url(r'^increment/(?P<slug>[-\w]+)/$', 'cart.views.increment_cart', name='increment_cart'),
    url(r'^decrement/(?P<slug>[-\w]+)/$', 'cart.views.decrement_cart', name='decrement_cart'),
    url(r'^update/(?P<slug>[-\w]+)/$', 'cart.views.update_cart', name='update_cart'),
    url(r'^remove/(?P<slug>[-\w]+)/$', 'cart.views.remove_from_cart', name='remove_from_cart'),
    url(r'^delete$', 'cart.views.delete', name='cart_empty'),
)
