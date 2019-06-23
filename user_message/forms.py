#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django import forms


class CommentForm(forms.Form):
	text = forms.CharField(label='写评论', max_length=200, widget=forms.Textarea(
		attrs={'class': 'form-control', 'placeholder': '在此输入评论', 'rows': '5'}))


