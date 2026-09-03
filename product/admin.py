from django.contrib import admin
from product.models import Product, Type, Size, Color

admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Color)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['title'] 