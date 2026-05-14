from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержание поста'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'category': 'Категория',
        }
        