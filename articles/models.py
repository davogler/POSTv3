from django.db import models
import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField
from django.core.urlresolvers import reverse

class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().exclude(status=self.model.DRAFT_STATUS)
		
class PublishedEntryManager(models.Manager):
	def get_query_set(self):
		return super(PublishedEntryManager, self).get_query_set().exclude(status=self.model.DRAFT_STATUS)

class DraftEntryManager(models.Manager):
    def get_query_set(self):
        return super(DraftEntryManager, self).get_query_set().filter(status=self.model.DRAFT_STATUS)

class Article(models.Model):
    """Model to store Articles"""
    PUBLISHED_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
        (PUBLISHED_STATUS, 'Published'),
        (DRAFT_STATUS, 'Draft'),
    )
    title = models.CharField(max_length=250)
    tagline = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    body = models.TextField()

    slug = models.SlugField(unique_for_date='pub_date')
    hero = FileBrowseField("Hero Image", max_length=200, extensions=[".jpg",".png", ".gif"], blank=True, null=True, help_text='Choose an huge image for this article. Minimum 1280px wide')
    screen = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey('Author', blank=True, null=True)
    photog = models.ForeignKey('Photog', blank=True, null=True)
    sponsor = models.ForeignKey('Sponsor', blank=True, null=True)
    more_info = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    special_js = models.TextField(blank=True)
    special_css = models.TextField(blank=True, help_text='Mainly h2.unique and p.tagline')
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    objects = models.Manager()	
    live = LiveEntryManager()
    draft = DraftEntryManager()
    published = PublishedEntryManager()
    
	
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Articles"
        #app_label = "blog"
		
    def __unicode__(self):
        return self.title
		
    def save(self, force_insert=False, force_update=False):
        #self.body_html = markdown(self.body)
        #if self.excerpt:
        #	self.excerpt_html = markdown(self.excerpt)
        super(Article, self).save(force_insert, force_update)
        
    @models.permalink	
    def get_absolute_url(self):
        return ('article_detail', (), {'slug': self.slug })
	

class Image(models.Model):
    article = models.ForeignKey('Article')
    name = models.CharField(max_length=35)
    image = FileBrowseField("Inline IMage", max_length=200, extensions=[".jpg",".png", ".gif"], blank=True, null=True, help_text='Inline image, yo.')


class Sponsor(models.Model):
    name = models.CharField(max_length=250)
    adimg = FileBrowseField("Ad Image", max_length=200, extensions=[".jpg",".png", ".gif"], blank=True, null=True, help_text='Upload an image to be used for advertising min width 250px')
    adlink = models.URLField()
    endorsement = models.TextField(blank=True) 
    instances = models.IntegerField(blank=True, null=True)
    paid_for = models.IntegerField(blank=True, null=True)
    add_date = models.DateTimeField(default=datetime.datetime.now())    
    
    class Meta:
        ordering = ['-add_date']
        verbose_name_plural = "Sponsors"
        #app_label = "blog"
    	
    def __unicode__(self):
        return self.name  
        
class Author(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(blank=True)
    colophon = models.TextField(blank=True) 
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Authors"
        #app_label = "blog"
    	
    def __unicode__(self):
        return self.name
        
class Photog(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(blank=True)
    colophon = models.TextField(blank=True) 
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Photographers"
        #app_label = "blog"
    	
    def __unicode__(self):
        return self.name         

