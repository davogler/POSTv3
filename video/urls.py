from django.conf.urls import patterns, include, url
from django.conf import settings
import video.views
from video.views import VideoDetail


urlpatterns = patterns('',
    url(r'^$', 'video.views.video_list', name='video_list'),
    url(r'^(?P<slug>[-\w]+)/$', VideoDetail.as_view(), name='video_detail'),
    #url(r'^rebuild/(?P<cart_id>[-\w]+)/$', 'cart.views.cart_rebuilder', name='cart_rebuilder'),
    #url(r'^add/(?P<slug>[-\w]+)/$', 'cart.views.add_to_cart', name='add_to_cart'),
    #url(r'^increment/(?P<slug>[-\w]+)/$', 'cart.views.increment_cart', name='increment_cart'),
    #url(r'^decrement/(?P<slug>[-\w]+)/$', 'cart.views.decrement_cart', name='decrement_cart'),
    #url(r'^update/(?P<slug>[-\w]+)/$', 'cart.views.update_cart', name='update_cart'),
    #url(r'^remove/(?P<slug>[-\w]+)/$', 'cart.views.remove_from_cart', name='remove_from_cart'),
    #url(r'^delete$', 'cart.views.delete', name='cart_empty'),
    #url(r'^checkout$', 'orders.views.czechout', name='czechout'),
    #url(r'^pay/(?P<order_id>[-\w]+)/$', orders.views.payout, name='payout'),
    #url(r'^hide_post/(?P<insta_id>[-\w]+)/$', insta.views.hide_media, name='hide_media'),
    #url(r'^tag/(?P<tag>[-\w]+)/$', insta.views.search_media, name='search_media'),
    #url(r'^subscribe_tag/(?P<tag>[-\w]+)/$', insta.views.instagram_subscribe, name='instagram_subscribe'),
    #url(r'^delete_tag/(?P<tag>[-\w]+)/$', insta.views.delete_igsubscription, name='delete_igsubscription'),
    #url(r'^hook/$', insta.views.process_tag_update, name='hook'),
)
