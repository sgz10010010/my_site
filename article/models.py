from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# 模型: 文章类型
class ArticleType(models.Model):
	# 类型名字
	type_name = models.CharField(max_length=20)

	def __str__(self):
		return '<文章类型: ' + str(self.type_name) + ' >'


# 模型: 文章
class Article(models.Model):
	# 标题
	title = models.CharField(max_length=50)
	# 内容
	content = RichTextField()
	# 文章类型
	article_type = models.ForeignKey(ArticleType, on_delete=models.DO_NOTHING)
	# 作者
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	# 阅读数
	read_count = models.IntegerField(default=0)
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True)
	# 更新时间
	update_time = models.DateTimeField(auto_now=True)
	is_deleted = models.NullBooleanField(default=False)

	def __str__(self):
		return '<文章: ' + str(self.title) + ' >'

	class Meta:
		ordering = ['-created_time']
