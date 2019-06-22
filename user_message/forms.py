#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django import forms


class ArticleCommentForm(forms.Form):
	text = forms.CharField(label='评论', max_length=200, widget=forms.Textarea(
		attrs={'class': 'form-control', 'placeholder': '在此输入评论', 'rows': '5'}))


class HomeMessageForm(forms.Form):
	text = forms.CharField(label='留言', max_length=400, widget=forms.Textarea(
		attrs={'class': 'form-control', 'placeholder': '在此输入留言', 'rows': '6'}))
