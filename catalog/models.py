from django.db import models
from filebrowser.fields import FileBrowseField
from django.utils.safestring import mark_safe
from filebrowser.settings import ADMIN_THUMBNAIL
from django.contrib.auth.models import User
import datetime


class Subscription(models.Model):
    ROLLING_ONE_YEAR = 1
    RENEWAL = 2
    OTHER = 3
    TYPE_CHOICES = (
        (ROLLING_ONE_YEAR, 'Rolling One Year'),
        (RENEWAL, 'Renewal'),
        (OTHER, 'Other')
    )
    title = models.CharField(max_length=200, default="One-Year Subscription")
    sku = models.CharField(max_length=200, help_text='Enter as pb[year][first month][second month]')
    term = models.IntegerField(default=4, help_text='default 4 issues in one year')
    type = models.IntegerField(choices=TYPE_CHOICES, default=ROLLING_ONE_YEAR)
    first_issue = models.IntegerField(help_text='Integer value of first issue')
    slug = models.SlugField(max_length=50, unique=True)
    price = models.FloatField(default=36.00, help_text='Cover Price')
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    image = FileBrowseField("Item Image", max_length=200, extensions=[
                            ".jpg", ".png", ".gif"], blank=True, null=True, help_text='Item Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'slug')
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        ordering = ['-first_issue']

    def __unicode__(self):
        return self.title

    # to do: function to get latest active instance

    def get_price(self):
        return self.price

    def get_queryset(self):
        return Subscription.objects.filter(client=self.request.user)

    def image_thumbnail(self):
        if self.image and self.image.filetype == "Image":
            return mark_safe('<img src="%s" />' % self.image.version_generate(ADMIN_THUMBNAIL).url)
        else:
            return ""
        thumb.short_description = 'Thumb'
        thumb.allow_tags = True

    #@models.permalink
    # def get_absolute_url(self):
    #    return ('product_detail', (), {'slug': self.slug})
