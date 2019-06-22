from django.contrib import admin
from .models import ArticleComment, HomeMessage


@admin.register(ArticleComment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'text', 'comment_time', 'article')
	ordering = ('-comment_time',)


@admin.register(HomeMessage)
class HomeMessageAdmin(admin.ModelAdmin):
	list_display = ('user', 'text', 'message_time')
	ordering = ('-message_time',)
