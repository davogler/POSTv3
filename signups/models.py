from django.db import models


class Subscriber(models.Model):
    """Model to store addresses for subscribers"""
    body = models.TextField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, unique=True)
    subscription_start = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.name)
             
    class Meta:
        verbose_name_plural = "Subscribers"
