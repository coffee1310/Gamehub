from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number', 'address', 'date_joined', 'last_login')

# Административный класс для модели ProductImage
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'updated_at',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')

class MouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'size', 'DPI', 'case_color', 'sensor_type', 'created_at', 'updated_at')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'advantages', 'disadvantages', 'created_at', 'updated_at')

admin.site.register(User, UserAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Mouse, MouseAdmin)
admin.site.register(Comments, CommentsAdmin)