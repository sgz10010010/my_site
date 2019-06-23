from django.contrib import admin
from .models import ArticleComment, ImageComment


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'text', 'comment_time', 'article')
	ordering = ('-comment_time',)


@admin.register(ImageComment)
class ImageCommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'text', 'comment_time', 'image')
	ordering = ('-comment_time',)
