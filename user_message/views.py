from django.contrib.auth.decorators import login_required
from .models import ArticleComment, HomeMessage
from article.models import Article
from django.shortcuts import redirect


@login_required
def add_article_comment(request):
	user = request.user
	text = request.POST.get('text')
	article_id = request.POST.get('article_id')
	referer = request.GET.get('from')

	comment = ArticleComment()
	comment.user = user
	comment.text = text
	comment.article = Article.objects.get(id=article_id)
	comment.save()
	return redirect(referer, '/')


@login_required
def add_home_message(request):
	user = request.user
	text = request.POST.get('text')
	referer = request.GET.get('from')

	home_message = HomeMessage()
	home_message.user = user
	home_message.text = text
	home_message.save()
	return redirect(referer, '/')
