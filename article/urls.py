#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path
from .views import article_detail, article_list, articles_with_type

urlpatterns = [
	path('article_list/', article_list, name='article_list'),
	path('articles_with_type/<int:type_id>', articles_with_type, name='articles_with_type'),
	path('article_detail/<int:article_id>', article_detail, name='article_detail'),
]