#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path
from .views import thumbnail, image_detail


urlpatterns = [
	path('thumbnail/', thumbnail, name='thumbnail'),
	path('image_detail/<int:image_id>', image_detail, name='image_detail'),
]
