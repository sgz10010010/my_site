from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from image.models import Image


class ArticleComment(models.Model):
	text = models.TextField()
	comment_time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, default='1')

	def __str__(self):
		return '<文章评论' + str(self.id) + ' >'

	class Meta:
		ordering = ['-comment_time']


class ImageComment(models.Model):
	text = models.TextField()
	comment_time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, default='1')

	def __str__(self):
		return '<图象评论' + str(self.id) + ' >'

	class Meta:
		ordering = ['-comment_time']
