from django.contrib import admin
from catalog.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('sku',), }
    list_display = ('title', 'first_issue', 'sku',)
    class Meta:
        model = Subscription


admin.site.register(Subscription, SubscriptionAdmin)


