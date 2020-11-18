from django.contrib import admin
from blog.models import Blog

class Blogadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  

admin.site.register(Blog, Blogadmin)