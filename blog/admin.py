from django.contrib import admin
from .models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_date' , 'id']
admin.site.register(Blog, BlogAdmin)