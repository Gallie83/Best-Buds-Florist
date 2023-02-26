from django import forms
from .models import BlogPost, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'intro', 'body']
        widgets = {
            'intro': forms.Textarea(attrs={'rows': 2}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }
