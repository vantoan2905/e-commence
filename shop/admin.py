from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', "image", 'price', 'articleNumber', 'articleType', 'productDisplayName', 'masterCategory', 'subCategory', 'gender', 'baseColour', 'fashionType', 'season', 'year', 'usag']  # Verify all fields exist
    
    
    
# register your models here.
admin.site.register(Product, ProductAdmin)
