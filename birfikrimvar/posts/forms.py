from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating and editing posts
    """
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Başlık giriniz'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Düşüncelerinizi paylaşın...',
                'rows': 5
            }),
        }
        labels = {
            'title': 'Başlık',
            'content': 'İçerik',
        }
        error_messages = {
            'title': {
                'required': 'Lütfen bir başlık giriniz.',
                'max_length': 'Başlık en fazla 200 karakter olabilir.'
            },
            'content': {
                'required': 'Lütfen içerik giriniz.'
            }
        }


class CommentForm(forms.ModelForm):
    """
    Form for creating comments
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Yorumunuzu yazın...',
                'rows': 3
            }),
        }
        labels = {
            'content': 'Yorum',
        }
        error_messages = {
            'content': {
                'required': 'Lütfen bir yorum giriniz.'
            }
        }