from django.contrib import admin
from orders.models import Order, Record, BackIssue


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'issue', 'originating_order')

    class Meta:
        model = Record


admin.site.register(Record, RecordAdmin)


class BackIssueAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'issue', 'quantity', 'originating_order')

    class Meta:
        model = BackIssue


admin.site.register(BackIssue, BackIssueAdmin)


