from django.contrib import admin
import models
from subscribers.models import Subscriber
from actions import export_as_csv_action



class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'charge_date',
                    'charge_id',
                    'cust_id',
                    'expires_on',
                    'street',
                    'city',
                    'state',
                    'zip',
                    )
    actions = [export_as_csv_action("CSV Export", fields=['name',
                                                          'email',
                                                          'charge_date',
                                                          'charge_id',
                                                          'cust_id',
                                                          'expires_on',
                                                          'street',
                                                          'city',
                                                          'state',
                                                          'zip',
                                                        ]
                                       )
               ]
               
    class Media:
        css = {'all': ('css/grap_extend.css',)}
        
admin.site.register(Subscriber, SubscriberAdmin)

