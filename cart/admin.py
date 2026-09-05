from django.contrib import admin
from .models import Cart, CartItem, DiscountModel

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['get_total_price']
    fields = ['product', 'size', 'color', 'quantity', 'price', 'get_total_price', 'is_paid']

    def get_total_price(self, obj):
        if obj and obj.price is not None:
            return f"{obj.get_total_price():,} $"
        return '0 $'
    get_total_price.short_description = 'Total Price'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'get_total_price',
        'get_final_price',
        'created_at',
        'updated_at',
    ]
    list_display_links = ['user']
    list_filter = ['created_at']
    search_fields = ['user__email']
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    inlines = [CartItemInline]

    def get_total_price(self, obj):
        return f"{obj.get_total_price():,} $"
    get_total_price.short_description = "Total Price"

    def get_final_price(self, obj):
        return f"{obj.get_final_price():,} $"
    get_final_price.short_description = "Final Price"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'size', 'color', 'quantity', 'price', 'get_total_price', 'is_paid']
    list_display_links = ['cart'] 
    list_filter = ['cart__user', 'size', 'color', 'is_paid']
    search_fields = ['product__title', 'cart__user__email']
    
    def get_total_price(self, obj):
        if obj and obj.price is not None:
            return f"{obj.get_total_price():,} $"
        return '0 $'
    get_total_price.short_description = 'Total Price'
    
    
@admin.register(DiscountModel)
class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'expiration_date', 'is_active']
    list_display_links = ['name'] 
    list_filter = ['is_active', 'expiration_date']
    search_fields = ['name', 'expiration_date']