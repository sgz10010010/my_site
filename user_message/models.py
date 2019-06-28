from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from image.models import Image
from ckeditor.fields import RichTextField


class ArticleComment(models.Model):
	text = RichTextField(verbose_name='评论内容')
	comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='评论者')
	article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, default='1', verbose_name='文章对象')

	def __str__(self):
		return '<文章评论' + str(self.id) + ' >'

	class Meta:
		ordering = ['-comment_time']
		verbose_name = '文章评论'
		verbose_name_plural = verbose_name


class ImageComment(models.Model):
	text = RichTextField(verbose_name='评论内容')
	comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='评论者')
	image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, default='1', verbose_name='图片对象')

	def __str__(self):
		return '<图象评论' + str(self.id) + ' >'

	class Meta:
		ordering = ['-comment_time']
		verbose_name = '图片评论'
		verbose_name_plural = verbose_name
