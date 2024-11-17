from .models import News_post
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое содержание'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите полное содержание'}),
        }



# строка для даты не нужна т.к она уже добавляется автоматически.
# смотри models.py - pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)