from django.db import models
from filebrowser.fields import FileBrowseField
import datetime
from articles.models import Article


class PublishedEntryManager(models.Manager):
    def get_queryset(self):
        return super(PublishedEntryManager, self).get_queryset().exclude(status=self.model.DRAFT_STATUS)

class DraftEntryManager(models.Manager):
    def get_queryset(self):
        return super(DraftEntryManager, self).get_queryset().filter(status=self.model.DRAFT_STATUS)

class VideoCategory(models.Model):
    name = models.CharField("Video Category Name", max_length=200, blank=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Video Category'
        verbose_name_plural = 'Video Categories'
        ordering = ['-timestamp',]

    def __unicode__(self):
        return self.name

class VideoCreator(models.Model):
    name = models.CharField("Video Person Name", max_length=200, blank=True)
    link = models.URLField(blank=True)
    colophon = models.TextField(blank=True) 
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Video Creators"
        
    def __unicode__(self):
        return self.name 





class VideoPost(models.Model):
    PUBLISHED_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
        (PUBLISHED_STATUS, 'Published'),
        (DRAFT_STATUS, 'Draft'),
    )
    POST_TYPE = 1
    COMMUNITY_TYPE = 2
    TYPE_CHOICES = (
        (POST_TYPE, 'POST Video'),
        (COMMUNITY_TYPE, 'Community Video'),
    )
    title = models.CharField("Video Title", max_length=200, blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=POST_TYPE)
    category = models.ManyToManyField('VideoCategory', blank=True)
    thumbnail = FileBrowseField("Thumbnail Image", max_length=200, extensions=[".jpg",".png", ".gif"], blank=True, null=True, help_text='For video list teaser, twoup size')
    vimeo_id = models.CharField("Vimeo ID", max_length=200, blank=True)
    youtube_id = models.CharField("Youtube ID", max_length=200, blank=True)
    creator = models.ManyToManyField('VideoCreator', blank=True)
    slug = models.SlugField()
    article = models.ForeignKey(Article, blank=True, null=True)
    caption_text = models.TextField("Caption", blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now, blank=True, help_text='Dictates sort order on video list')
    sticky = models.BooleanField(default=False)
    template_name = models.CharField(max_length=250, blank=True, help_text='enter optional template to override default')
    timestamp = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    
    objects = models.Manager()  
    draft = DraftEntryManager()
    published = PublishedEntryManager()

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['-pub_date', ]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.timestamp = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        return super(VideoPost, self).save(*args, **kwargs)

    @models.permalink   
    def get_absolute_url(self):
        return ('video_detail', (), {'slug': self.slug })
