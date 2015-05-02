import datetime

from django.db import models
from django.contrib.auth.models import User
from catalog.models import Subscription
from articles.models import Issue
from customers.models import Recipient

class CartItemSubscriptionManager(models.Manager):
    def get_queryset(self):
        return super(CartItemSubscriptionManager, self).get_queryset().filter(single__isnull=True)

class CartItemSingleManager(models.Manager):
    def get_queryset(self):
        return super(CartItemSingleManager, self).get_queryset().filter(subscription__isnull=True)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    active = models.BooleanField(default=True)
    product_total = models.FloatField(default=0.00)
    shipping_total = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)

    item_list = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Cart id: %s" % (self.id)

    def items_as_list(self):
        list = self.item_list.split("', '")
        cleanlist = map(lambda each: each.strip("]").strip("['"), list)
        # return self.item_list.split("',").strip(']')
        return cleanlist


class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    flug = models.SlugField(max_length=50, null=True, blank=True)
    subscription = models.ForeignKey(Subscription, null=True, blank=True)
    single = models.ForeignKey(Issue, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.FloatField(default=0.00)
    shipping_line_total = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    objects = models.Manager()  
    subbie_type = CartItemSubscriptionManager()
    single_type = CartItemSingleManager()
    recipient = models.ForeignKey(Recipient, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)

    