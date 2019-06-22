from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import auth
from django.urls import reverse


# 视图:登入
def login(request):
	if request.method == 'GET':
		request.session['from'] = request.META.get('HTTP_REFERER', reverse('home'))
		login_form = LoginForm()
	elif request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				response = redirect(reverse('success_login'))
				return response
			else:
				login_form.add_error(None, '用户名或密码不正确')

	context = dict()
	context['login_form'] = login_form
	response = render(request, 'user/login.html', context)
	return response


def success_login(request):
	response = render(request, 'user/success_login.html')
	return response


# 视图:登出
def logout(request):
	auth.logout(request)
	response = redirect(reverse('home'))
	return response


# 视图:注册
def register(request):
	if request.method == 'GET':
		request.session['from'] = request.META.get('HTTP_REFERER', reverse('home'))
		register_form = RegisterForm()
	elif request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			password = register_form.cleaned_data['password']
			auth.models.User.objects.create_user(username=username, password=password)
			user = auth.authenticate(username=username, password=password)
			auth.login(request, user)
			response = redirect(reverse('success_login'))
			return response

	context = dict()
	context['register_form'] = register_form
	response = render(request, 'user/register.html', context)
	return response
