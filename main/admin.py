from django.contrib import admin
# from django.utils.text import slugify
# Register your models here.
from .models import MenuItem


# admin.site.register(MenuItem)
# @admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(MenuItem, MenuItemAdmin)