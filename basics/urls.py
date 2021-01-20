from django.contrib import admin
from django.urls import path
from basics import views

urlpatterns = [
    path('',views.starter, name="starter"),
]
