from django.shortcuts import render, get_object_or_404
from .models import Image
from django.db.models.aggregates import Count
from my_site.common import list_display
from user_message.models import ImageComment
from user_message.forms import CommentForm


def thumbnail(request):
	images = Image.objects.annotate(comment_num=Count('imagecomment'))
	context = list_display(request, images, 20)
	context['images'] = images
	response = render(request, "image/thumbnail.html", context)
	return response


def image_detail(request, image_id):
	image = get_object_or_404(Image, id=image_id)
	comments = ImageComment.objects.filter(image_id=image_id)
	# 阅读数计数
	if not request.COOKIES.get('image_' + str(image_id)) == 'read':
		image.read_count += 1
		image.save()
	# 上下文
	context = list_display(request, comments, 8)
	context['image'] = image
	context['read_count'] = image.read_count
	context['prev_image'] = Image.objects.filter(created_time__gt=image.created_time).last()
	context['next_image'] = Image.objects.filter(created_time__lt=image.created_time).first()
	context['comment_form'] = CommentForm()
	context['comments'] = comments

	response = render(request, 'image/image_detail.html', context)
	response.set_cookie('image_' + str(image_id), 'read')
	return response

