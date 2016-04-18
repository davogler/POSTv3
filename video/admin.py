from django.contrib import admin

from video.models import VideoPost, VideoCategory, VideoCreator


class VideoPostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    class Meta:
        model = VideoPost

    list_display = ('title','status','type', 'pub_date'  )
    list_editable = ('status',)
    

admin.site.register(VideoPost, VideoPostAdmin)


class VideoCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = VideoCategory

    list_display = ('name', )
    

admin.site.register(VideoCategory, VideoCategoryAdmin)

class VideoCreatorAdmin(admin.ModelAdmin):
    class Meta:
        model = VideoCreator

    list_display = ('name', )
    

admin.site.register(VideoCreator, VideoCreatorAdmin)
