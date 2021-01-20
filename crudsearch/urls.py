from django.contrib import admin
from django.urls import path
from crudsearch import views

urlpatterns = [
    path('',views.crudsearch, name="crudsearch"),
    path('student/',views.crudsearch_student, name="crudsearch_student"),
    path('add_project/',views.crudsearch_add_project, name="crudsearch_add_project"),
    path('add_student/',views.crudsearch_add_student, name="crudsearch_add_student"),
]
