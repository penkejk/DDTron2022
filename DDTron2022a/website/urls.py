from django.contrib import admin
from django.urls import path, include
from website.views import person_view, main_view

urlpatterns = [
    path('<int:pk>', person_view, name = "person"),
    path('', main_view, name = "main"),
]