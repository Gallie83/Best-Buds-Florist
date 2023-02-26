from django import forms
from .models import BlogPost, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'intro', 'body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }
