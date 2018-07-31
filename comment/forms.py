from django import forms

from .models import Comment


class commentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'content']
