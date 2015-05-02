from django.contrib import admin
from cart.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)



class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id',  'cart', 'subscription', 'single', 'quantity')

    class Meta:
        model = CartItem


admin.site.register(CartItem, CartItemAdmin)
