from django.contrib import admin
from django.urls import path, include
from website.views import person_view

urlpatterns = [
    path('<int:pk>', person_view, name = "person")
]