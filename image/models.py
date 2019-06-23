from django.db import models
from django.contrib.auth.models import User


# 模型: 图象
class Image(models.Model):
	# 图象
	image = models.ImageField(upload_to='images/')
	# 名字
	name = models.CharField(max_length=30)
	# 作者
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	# 描述
	description = models.CharField(max_length=200)
	# 阅读数
	read_count = models.IntegerField(default=0)
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True)
	is_deleted = models.NullBooleanField(default=False)

	def __str__(self):
		return '<图象: ' + str(self.name) + ' >'

	class Meta:
		ordering = ['-created_time']
