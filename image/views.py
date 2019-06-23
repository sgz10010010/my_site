from django.shortcuts import render
from .models import Image
from django.db.models.aggregates import Count
from my_site.common import list_display



def thumbnail(request):
	images = Image.objects.annotate(comment_num=Count('articlecomment'))
	context = list_display(request, images)
	context['images'] = images
	response = render(request, "", context)

def image_detail(request):
	pass