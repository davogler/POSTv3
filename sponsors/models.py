from django.db import models
import datetime
from django.utils.timezone import now
from filebrowser.fields import FileBrowseField

class Advert(models.Model):
    name = models.CharField(max_length=250)
    adimg = FileBrowseField("Ad Image", max_length=200, extensions=[".jpg",".png", ".gif"], blank=True, null=True, help_text='Upload an image to be used for advertising: 768x90')
    adlink = models.URLField() 
    position = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    add_date = models.DateTimeField(default=now)    
    
    class Meta:
        ordering = ['-add_date']
        verbose_name_plural = "Advertisement Banners"
        
    def __unicode__(self):
        return self.name  
