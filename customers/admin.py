from django.contrib import admin
from customers.models import Recipient, CreditCard, Comp


class RecipientAdmin(admin.ModelAdmin):
    class Meta:
        model = Recipient


admin.site.register(Recipient, RecipientAdmin)

class CompAdmin(admin.ModelAdmin):
    class Meta:
        model = Comp


admin.site.register(Comp, CompAdmin)


class CreditCardAdmin(admin.ModelAdmin):
    class Meta:
        model = CreditCard


admin.site.register(CreditCard, CreditCardAdmin)


