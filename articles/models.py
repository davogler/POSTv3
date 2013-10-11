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
    author = models.ForeignKey(User)
    featured = models.BooleanField(default=False)
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
	
        

