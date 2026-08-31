from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['get_total_price']
    fields = ['product', 'size', 'color', 'quantity', 'price', 'get_total_price']

    def get_total_price(self, obj):
        if obj and obj.price is not None:
            return f"{obj.get_total_price():,} $"
        return '0 $'
    get_total_price.short_description = 'Total Price'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at', 'get_total_price', 'get_total_items', 'is_paid']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['user__email']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CartItemInline]
    
    def get_total_price(self, obj):
        total = obj.get_total_price()
        return f"{total:,} $" if total else '0 $'
    get_total_price.short_description = 'Total Price'
    
    def get_total_items(self, obj):
        return obj.get_total_items() or 0
    get_total_items.short_description = 'Number of Items'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'size', 'color', 'quantity', 'price', 'get_total_price']
    list_filter = ['cart__user', 'size', 'color']
    search_fields = ['product__title', 'cart__user__email']
    
    def get_total_price(self, obj):
        if obj and obj.price is not None:
            return f"{obj.get_total_price():,} $"
        return '0 $'
    get_total_price.short_description = 'Total Price'