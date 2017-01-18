from django.db import models
from django.conf import settings
from datetime import date



# Create your models here.


class CreditCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    default = models.BooleanField(default=True)
    first_name = models.CharField("Payer first name", max_length=45, blank=True)
    last_name = models.CharField("Payer last name", max_length=45, blank=True)
    payer_name = models.CharField("Payer full name", max_length=250, blank=True)
    payer_email = models.CharField("Payer full name", max_length=200, blank=True)
    stripe_id = models.CharField(max_length=120, null=True, blank=True)
    last4 = models.CharField(max_length=120)
    card_type = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Credit Card'
        verbose_name_plural = 'Credit Cards'
        ordering = ['-timestamp', ]
        #unique_together = ("user", "default")

    def __unicode__(self):
        return self.last4

    def save(self, *args, **kwargs):
        if self.default:
            try:
                temp = CreditCard.objects.get(default=True)
                if self != temp:
                    temp.default = False
                    temp.save()
            except CreditCard.DoesNotExist:
                pass
        super(CreditCard, self).save(*args, **kwargs)

class Recipient(models.Model):

    """Model to store recipients"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    first_name = models.CharField("First Name", max_length=45, blank=True)
    last_name = models.CharField("Last Name", max_length=45, blank=True)
    org = models.CharField("Organization/Business", max_length=45, blank=True)
    address_line1 = models.CharField("Address line 1", max_length=45, blank=True)
    address_line2 = models.CharField("Address line 2", max_length=45, blank=True)
    postal_code = models.CharField("Postal Code", max_length=10, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state_province = models.CharField("State/Province", max_length=40,
                                      blank=True)
    country = models.CharField("Country", max_length=40,
                               blank=True)

    def __unicode__(self):
        if self.org:
            return "%s %s, %s" % (self.first_name, self.last_name, self.org)
        else:
            return "%s %s" % (self.first_name, self.last_name)

    def get_address(self):
        return "%s %s, %s, %s, %s, %s, %s, %s" %(self.first_name, self.last_name, self.org, self.address_line1, self.address_line2, self.city, self.state_province, self.postal_code)

    class Meta:
        verbose_name_plural = "Recipients"

