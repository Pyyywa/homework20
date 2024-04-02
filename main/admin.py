from django.contrib import admin

from main.models import Product, Category

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity_per_unit', 'category')
    search_fields = ('product_name',  'desc')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
