from django.contrib import admin
from blog.models import Blog, Comment, Preference, BlogCategory

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Preference)
admin.site.register(BlogCategory)
