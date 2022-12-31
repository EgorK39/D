from django.urls import include, path
from .views import MySignupView

urlpatterns = [
    path("signup/", MySignupView.as_view()),
]
