from django.contrib import admin
from sponsors.models import Advert

class AdvertAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Advert

    list_display = ('name','position', 'is_active',  )
    list_editable = ('is_active',)
    

admin.site.register(Advert, AdvertAdmin)

