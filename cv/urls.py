# cv/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_view, name='cv_home'),  # Hlavní stránka Domů
    path('about/', views.about_view, name='about'),  # Stránka O mně
    path('hearthstone/', views.hearthstone_view, name='hearthstone'),  # Hearthstone stránka
    path('kontakt/', views.kontakt_view, name='kontakt'), # Stránka Kontakt
]