from django import forms
from .models import Post


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class DeletePostForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
