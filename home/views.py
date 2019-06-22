from django.shortcuts import render
from article.models import Article
from django.db.models.aggregates import Count
from user_message.models import HomeMessage
from user_message.forms import HomeMessageForm
from my_site.common import list_display
from django.http import FileResponse


def home(request):
	home_message = HomeMessage.objects.all()
	context = list_display(request, home_message)
	context['articles'] = Article.objects.annotate(comment_num=Count('articlecomment'))[0:9]
	context['home_message'] = home_message
	context['home_message_form'] = HomeMessageForm()
	response = render(request, 'home/home.html', context)
	return response


def picture(request):
	return render(request, 'home/picture.html')


def cv_download(request):
	file = open('static/sgz_cv.pdf', 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="sgz_cv.pdf"'
	return response
