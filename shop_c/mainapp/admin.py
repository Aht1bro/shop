from django.contrib import admin

from .models import *

class SlideAdmin(admin.ModelAdmin):
    list_display=('id',"image","title",'sub_title')
    list_display_links = ('id', 'title')
    search_fields=('title', 'image')

class ProductAdmin(admin.ModelAdmin):
    list_display=('id',"image","title",'category')
    list_display_links = ('id', 'title')
    search_fields=('title', 'category')
    list_filter=('title', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slide, SlideAdmin)