from django.urls import path
from . import views


urlpatterns = [
    path('', views.Calculator.as_view()),
]