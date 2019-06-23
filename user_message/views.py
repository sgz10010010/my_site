from django.contrib.auth.decorators import login_required
from .models import ArticleComment, ImageComment
from article.models import Article
from image.models import Image
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
def add_image_comment(request):
	user = request.user
	text = request.POST.get('text')
	article_id = request.POST.get('image_id')
	referer = request.GET.get('from')

	comment = ImageComment()
	comment.user = user
	comment.text = text
	comment.image = Image.objects.get(id=article_id)
	comment.save()
	return redirect(referer, '/')