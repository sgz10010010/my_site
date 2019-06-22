#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(label='用户名', min_length=3, max_length=12, widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': '用户名长度3-12'}))
	password = forms.CharField(label='密码', min_length=8, max_length=16, widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': '密码长度8-16'}))


class RegisterForm(forms.Form):
	username = forms.CharField(label='*用户名', min_length=3, max_length=12, widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': '用户名长度3-12'}))
	password = forms.CharField(label='*密码', min_length=8, max_length=16, widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': '密码长度8-16'}))
	password_again = forms.CharField(label='*确认密码', min_length=8, max_length=16, widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': '再输入一次密码'}))

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('用户名已存在')
		else:
			return username

	def clean_password_again(self):
		password = self.cleaned_data['password']
		password_again = self.cleaned_data['password_again']
		if password != password_again:
			raise forms.ValidationError('两次输入密码不一致')
		else:
			return password_again

	def clean_email(self):
		email = self.cleaned_data['email']
		if (email != '') and (User.objects.filter(email=email).exists()):
			raise forms.ValidationError('邮箱已存在')
		else:
			return email
