from django.contrib import admin
from .models import ArticleType, Article


# 后台的文章类模型,继承自模型模块的文章类模型
@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'type_name')


# 后台的文章模型,继承自模型模块的文章模型
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'article_type', 'author', 'read_count', 'is_deleted', 'created_time', 'update_time', )
	ordering = ('-id',)