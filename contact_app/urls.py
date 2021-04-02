from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormApi.as_view()),
]
