# To get the urls.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    # About
    path('about/', views.about_view, name="about"),
    # Programs
    path('programs/', views.programs_view, name="programs")
]