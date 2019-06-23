from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleType
from django.db.models.aggregates import Count
from user_message.models import ArticleComment
from user_message.forms import CommentForm
from my_site.common import list_display


# 视图: 文章详情
def article_detail(request, article_id):
	article = get_object_or_404(Article, id=article_id)
	comments = ArticleComment.objects.filter(article_id=article_id)
	# 阅读数计数
	if not request.COOKIES.get('article_' + str(article_id)) == 'read':
		article.read_count += 1
		article.save()
	# 上下文
	context = list_display(request, comments)
	context['article'] = article
	context['read_count'] = article.read_count
	context['prev_article'] = Article.objects.filter(created_time__gt=article.created_time).last()
	context['next_article'] = Article.objects.filter(created_time__lt=article.created_time).first()
	context['comment_form'] = CommentForm()
	context['comments'] = comments
	context['type_list'] = ArticleType.objects.annotate(article_num=Count('article'))

	response = render(request, 'article/article_detail.html', context)
	response.set_cookie('article_' + str(article_id), 'read')
	return response


# 视图: 所有文章列表
def article_list(request):
	articles = Article.objects.annotate(comment_num=Count('articlecomment'))
	context = list_display(request, articles)
	context['articles'] = articles
	context['type_list'] = ArticleType.objects.annotate(article_num=Count('article'))
	response = render(request, "article/article_list.html", context)
	return response


# 视图: 指定文章类型的文章列表
def articles_with_type(request, type_id):
	type_name = ArticleType.objects.get(id=type_id).type_name
	articles = Article.objects.filter(article_type=type_id)
	context = list_display(request, articles)
	context['articles'] = articles
	context['type_name'] = type_name
	context['type_list'] = ArticleType.objects.annotate(article_num=Count('article'))
	response = render(request, "article/articles_with_type.html", context)
	return response

