from django.db import models
#from orders.models import Order


class Subscriber(models.Model):
    """Model to store addresses for subscribers"""
    #orders = models.ManyToManyField(Order)
    name = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    cust_id = models.CharField(max_length=255,  blank=True)
    charge_id = models.CharField(max_length=255, blank=True, unique=True)
    charge_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.name)
             
    class Meta:
        verbose_name_plural = "Subscribers"

