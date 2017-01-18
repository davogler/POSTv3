from django.conf.urls import patterns, include, url
from django.conf import settings
import cart.views
import orders.views
from customers.views import *

urlpatterns = patterns('',
    #url(r'^$', 'orders.views.checkout', name='checkout'),
    url(r'add/$', 'customers.views.add_recipient', name='add_recipient'),
    url(r'add_existing/$', 'customers.views.add_existing_recipient', name='add_existing_recipient'),
    url(r'edit/$', 'customers.views.edit_recipient', name='edit_recipient'),
    url(r'delete/(?P<pk>[-\w\d]+)/$', 'customers.views.delete_recipient', name='delete_recipient'),
    url(r'delete_cc/(?P<pk>[-\w\d]+)/$', 'customers.views.delete_creditcard', name='delete_creditcard'),

)
