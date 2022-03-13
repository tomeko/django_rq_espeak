#django_rq_espeak_app urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('espeak', views.espeak),
    path('check', views.checkstatus)
]