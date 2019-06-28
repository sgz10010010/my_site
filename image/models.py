from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# 模型: 图象
class Image(models.Model):
	# 图象
	image = models.ImageField(upload_to='images/%Y/%m/%d/')
	# 名字
	name = models.CharField(max_length=30, verbose_name='名字')
	# 作者
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
	# 描述
	description = RichTextField(verbose_name='描述')
	# 阅读数
	read_count = models.IntegerField(default=0, verbose_name='阅读数')
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
	is_deleted = models.NullBooleanField(default=False, verbose_name='删除状态')

	def __str__(self):
		return '<图象: ' + str(self.name) + ' >'

	class Meta:
		ordering = ['-created_time']
		verbose_name = '图片'
		verbose_name_plural = verbose_name
