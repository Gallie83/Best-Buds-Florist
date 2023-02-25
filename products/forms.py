from django import forms
from .models import Product, ReviewRating
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['title', 'review', 'rating']
