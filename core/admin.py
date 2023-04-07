from django.contrib import admin
from .models import *
 
# Register your models here.

@admin.register(Blog_Model)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','author', 'image']