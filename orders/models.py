from django.db import models
from django.conf import settings



from cart.models import Cart, CartItem
from customers.models import Recipient, CreditCard



STATUS_CHOICES = (
    ("Started", "Started"),
    ("Pending", "Pending"),
    ("Finished", "Finished"),
    ("Refunded", "Refunded"),
)



# class OrderItem(models.Model):
#     cart_item = models.ForeignKey(CartItem)
#     recipient = models.ForeignKey(Recipient, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#     class Meta:
#         verbose_name = 'Order Item'
#         verbose_name_plural = 'Order Items'
#         ordering = ['-timestamp', ]

#     def __unicode__(self):
#         return self.last4

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC123', unique=True)
    #credit_card = models.ForeignKey(CreditCard, null=True, blank=True)
    cart = models.ForeignKey(Cart)
    total = models.FloatField(default=0.00)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    main_recipient = models.ForeignKey(Recipient, null=True, blank=True)
    notes = models.TextField("Comments", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-timestamp', ]

    def __unicode__(self):
        return self.order_id

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('order_detail', args=[self.order_id])

