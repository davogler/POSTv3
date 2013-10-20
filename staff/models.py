from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    webname = models.CharField(max_length=250, help_text='somethin.com')
    weblink = models.URLField(blank=True, null=True)
    twithandle = models.CharField(max_length=250, help_text='just the @ and name')
    twitlink = models.URLField(blank=True, null=True)
    lionlink = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, help_text='form of 585.555.1212')
    position = models.IntegerField()
    
    def save(self, *args, **kwargs):
            model = self.__class__
            
            if self.position is None:
                # Append
                try:
                    last = model.objects.order_by('-position')[0]
                    self.position = last.position + 1
                except IndexError:
                    # First row
                    self.position = 0
            
            return super(Staff, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('position',)
    
    def __unicode__(self):
        return self.name

