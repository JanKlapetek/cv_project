# cv/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_view, name='cv_view'),
    path('about_view/', views.about_view, name='about_view'),
]