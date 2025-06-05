from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)