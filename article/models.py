from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# 模型: 文章类型
class ArticleType(models.Model):
	# 类型名字
	type_name = models.CharField(max_length=20, verbose_name='文章类型')

	def __str__(self):
		return str(self.type_name)
		
	class Meta:
				verbose_name = '文章类型'
				verbose_name_plural = verbose_name

# 模型: 文章
class Article(models.Model):
	# 标题
	title = models.CharField(max_length=50, verbose_name='标题')
	# 内容
	content = RichTextUploadingField(verbose_name='内容')
	# 文章类型
	article_type = models.ForeignKey(ArticleType, on_delete=models.DO_NOTHING, verbose_name='文章类型')
	# 作者
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
	# 阅读数
	read_count = models.IntegerField(default=0, verbose_name='阅读数')
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
	# 更新时间
	update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
	is_deleted = models.NullBooleanField(default=False, verbose_name='删除状态')

	def __str__(self):
		return str(self.title)

	class Meta:
		ordering = ['-created_time']
		verbose_name = '文章'
		verbose_name_plural = verbose_name


class ArticleImage(models.Model):
		content = RichTextUploadingField(verbose_name='内容')
