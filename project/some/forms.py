from django import forms
from .models import PostModel, Comment
from django.core.exceptions import ValidationError
from pprint import pprint


class PostForm(forms.ModelForm):
    title = forms.CharField(help_text="Введите заголовок объявления")
    text = forms.CharField(min_length=12, help_text='Введите тест своего объявления.'
                                                    'не должен быть короче 12 символов')

    class Meta:
        model = PostModel
        fields = [
            'category',
            'title',
            'text',
            'photo',
            'file',
        ]

    def clean(self):
        cleaned_data = super().clean()  # Данные, которые ввел пользователь
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        pprint(cleaned_data)  # FIXME
        if text == title:
            raise ValidationError({
                'text': 'Название не должно совпадать с текстом объявления'
            })
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
