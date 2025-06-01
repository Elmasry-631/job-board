from django.contrib import admin

# Register your models here.

from .models import AddProduct
@admin.register(AddProduct)
class AddProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'created_at')
    search_fields = ('product_name',)
    prepopulated_fields = {'slug': ('product_name',)}
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    