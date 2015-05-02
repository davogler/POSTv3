from django.contrib import admin
from insta.models import InstaPost, IGTag, BadPerson


class InstaPostAdmin(admin.ModelAdmin):
    class Meta:
        model = InstaPost

    list_display = ('insta_id', 'username', 'tag', 'active',)
    list_editable = ['active',]


admin.site.register(InstaPost, InstaPostAdmin)


class IGTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'ig_id', 'shown_in_articles',)

    class Meta:
        model = IGTag


admin.site.register(IGTag, IGTagAdmin)


class BadPersonAdmin(admin.ModelAdmin):
    list_display = ('username',)

    class Meta:
        model = BadPerson


admin.site.register(BadPerson, BadPersonAdmin)
