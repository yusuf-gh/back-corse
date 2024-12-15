from django.contrib import admin
from .models import Category, Product, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    ordering = ('name',)
    list_editable = ('price', 'stock')

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'is_main', 'order')
    search_fields = ('product__name',)
    list_filter = ('product', 'is_main')
    ordering = ('order',)

admin.site.register(ProductImage, ProductImageAdmin)
