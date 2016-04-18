from django.db import models
from django.conf import settings



from cart.models import Cart, CartItem
from customers.models import Recipient, CreditCard



STATUS_CHOICES = (
    ("Started", "Started"),
    ("Pending", "Pending"),
    ("Finished", "Finished"),
    ("Recorded", "Recorded"),
    ("Refunded", "Refunded"),
)



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC123', unique=True)
    #credit_card = models.ForeignKey(CreditCard, null=True, blank=True)
    cart = models.ForeignKey(Cart)
    payer_name = models.CharField(max_length=120)
    payer_email = models.EmailField()
    total = models.FloatField(default=0.00)
    shipping = models.FloatField(default=0.00)
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

class Record(models.Model):
    recipient = models.ForeignKey(Recipient, null=True, blank=True)
    originating_order = models.ForeignKey(Order, null=True, blank=True)
    issue = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        ordering = ['-timestamp', ]

    def __unicode__(self):
        return "%s %s" % (self.recipient.first_name, self.recipient.last_name)

class BackIssue(models.Model):
    recipient = models.ForeignKey(Recipient, null=True, blank=True)
    originating_order = models.ForeignKey(Order, null=True, blank=True)
    issue = models.IntegerField()
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Back Issue'
        verbose_name_plural = 'Back Issues'
        ordering = ['-timestamp', ]

    def __unicode__(self):
        return "%s %s" % (self.recipient.first_name, self.recipient.last_name)

