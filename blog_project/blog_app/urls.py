# To get the urls.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    # About
    path('about/', views.about_view)
]