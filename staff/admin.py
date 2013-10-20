from django.contrib import admin
from staff.models import Staff

class StaffAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/admin_list_reorder.js',
        )
    
    list_display = ('position','name','title',)   # Don't forget to add the other fields that should be displayed in the list view here
    list_display_links = ('name',)
    list_editable = ('position',)  # 'position' is the name of the model field which holds the position of an element

admin.site.register(Staff, StaffAdmin)