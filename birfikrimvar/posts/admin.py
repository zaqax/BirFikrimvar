from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at', 'get_likes_count', 'get_comments_count')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username')
    date_hierarchy = 'created_at'
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    get_likes_count.short_description = 'Beğeniler'
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    get_comments_count.short_description = 'Yorumlar'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'user__username', 'post__title')
    date_hierarchy = 'created_at'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'post__title')
    date_hierarchy = 'created_at'