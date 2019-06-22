#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django.core.paginator import Paginator


# 函数: 把对象集合分页
def list_display(request, objs):
	# 指定页码
	page_num = int(request.GET.get('page', 1))
	paginator = Paginator(objs, 10)
	# 指定页
	page_now = paginator.get_page(page_num)
	# 总页数
	page_count = paginator.num_pages
	# 页码显示范围
	if page_num <= 5:
		page_range = list(range(1, min(9, page_count) + 1))
	elif 5 < page_num and page_count <= 9:
		page_range = list(range(1, page_count + 1))
	else:
		page_range = list(range(page_num - 4, min(page_num + 4, page_count + 1)))
	# 上下文
	context = dict()
	context['page_now'] = page_now
	context['page_num'] = page_num
	context['page_count'] = page_count
	context['page_range'] = page_range
	return context