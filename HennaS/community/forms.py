from django import forms
from .models import Post, Comment
from products.widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)

    image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)
