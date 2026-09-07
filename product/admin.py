from django.contrib import admin
from product.models import Product, Category, Size, Color


admin.site.register(Size)
admin.site.register(Color)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['title']
  
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'slug']
    list_display_links = ['title']