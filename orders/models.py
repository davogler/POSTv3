from django.db import models
from django.conf import settings



from cart.models import Cart


STATUS_CHOICES = (
    ("Started", "Started"),
    ("Pending", "Pending"),
    ("Finished", "Finished"),
    ("Refunded", "Refunded"),
)


class Order(models.Model):
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=2)
    order_id = models.CharField(max_length=120, default='ABC123', unique=True)
    
    cart = models.ForeignKey(Cart)
    total = models.FloatField(default=0.00)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    requires_shipping = models.BooleanField(default=False) 
    notes = models.TextField("Comments", null=True, blank=True)
    last4 = models.CharField(max_length=120)
    card_type = models.CharField(max_length=120)
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
