from django.db import models

# Create your models here.


class Recipient(models.Model):

    """Model to store recipients"""
    first_name = models.CharField("Address line 1", max_length=45, blank=True)
    last_name = models.CharField("Address line 1", max_length=45, blank=True)
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
        return "%s %s %s" % (self.first_name, self.last_name, self.org)

    class Meta:
        verbose_name_plural = "Recipients"
