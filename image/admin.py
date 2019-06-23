from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'author', 'description', 'read_count', 'is_deleted', 'created_time',)
	ordering = ('-id',)