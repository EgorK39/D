from pprint import pprint

from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(label='Имя', min_length=3)
    last_name = forms.CharField(label='Фамилия', min_length=3)
    username = forms.CharField(label='Логин', min_length=1, max_length=100)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        """ Моя обработка """
        pprint(user)
        return user

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            raise ValidationError({
                'first_name': 'Поля "Имя" и "Фамилия" не должны быть одинаковыми'
            })

        return cleaned_data
