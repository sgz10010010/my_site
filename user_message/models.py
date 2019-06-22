from django.db import models
from django.contrib.auth.models import User
from article.models import Article


class ArticleComment(models.Model):
	text = models.TextField()
	comment_time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, default='1')

	def __str__(self):
		return '<文章评论,id: ' + str(self.id) + ' >'

	class Meta:
		ordering = ['-comment_time']


class HomeMessage(models.Model):
	text = models.TextField()
	message_time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

	def __str__(self):
		return '<首页留言,id: ' + str(self.id) + ' >'

	class Meta:
		ordering = ['-message_time']
