from django import forms
from .models import Post, Comment
from products.widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('heading', 'body', 'image', 'user_profile')

    image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'user_profile', 'for_post')
