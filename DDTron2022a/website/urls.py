from django.contrib import admin
from django.urls import path, include
from website.views import person_view, main_view, group_view

urlpatterns = [

    path('group/<int:pk>', group_view, name = "group"),
    path('', main_view, name = "main"),
    path('person/<int:pk>', person_view, name = "person"),
]