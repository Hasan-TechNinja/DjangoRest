from django.contrib import admin
from . models import Blog, Comment

# Register your models here.

class BlogModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'body', 'created'
    )
admin.site.register(Blog, BlogModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'blog', 'comment'
    )
admin.site.register(Comment, CommentModelAdmin)