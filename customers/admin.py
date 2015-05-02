from django.contrib import admin
from customers.models import Recipient


class RecipientAdmin(admin.ModelAdmin):
    class Meta:
        model = Recipient


admin.site.register(Recipient, RecipientAdmin)


