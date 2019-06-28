from django.shortcuts import render
from django.http import FileResponse


def home(request):
	response = render(request, 'home/home.html')
	return response


def cv_download(request):
	file = open('static/sgz_cv.pdf', 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="sgz_cv.pdf"'
	return response

def contact_me(request):
	return render(request, 'home/contact_me.html')
