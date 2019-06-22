#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path
from .views import add_article_comment, add_home_message

urlpatterns = [
	path('add_article_comment/', add_article_comment, name='add_article_comment'),
	path('add_home_message/', add_home_message, name='add_home_message'),
]
