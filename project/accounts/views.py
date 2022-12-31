from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import MyCustomSignupForm
from allauth.account.views import SignupView


class MySignupView(SignupView):
    form_class = MyCustomSignupForm
    template_name = "account/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['count'] = User.objects.all().count()
        return context
