from django.contrib import admin
from customers.models import Recipient, CreditCard


class RecipientAdmin(admin.ModelAdmin):
    class Meta:
        model = Recipient


admin.site.register(Recipient, RecipientAdmin)


class CreditCardAdmin(admin.ModelAdmin):
    class Meta:
        model = CreditCard


admin.site.register(CreditCard, CreditCardAdmin)


