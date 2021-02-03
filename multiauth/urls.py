from django.contrib import admin
from django.urls import path
from multiauth import views

urlpatterns = [
    path('',views.multiauth, name="multiauth"),
    path('student/',views.multiauth_student, name="multiauth_student"),
    path('teacher/',views.multiauth_teacher, name="multiauth_teacher"),
    path('register/student/',views.multiauth_register_student, name="multiauth_register_student"),
    path('register/teacher/',views.multiauth_register_teacher, name="multiauth_register_teacher"),
    path('login/',views.multiauth_login, name="multiauth_login"),
    path('logout/',views.multiauth_logout, name="multiauth_logout"),
    path('no_access/',views.no_access, name="no_access"),
    path('student/profile/picture',views.update_student_profile_picture, name="update_student_profile_picture"),
    path('student/profile/update',views.update_student_details, name="update_student_details"),
    path('student/profile/deleteAccount',views.delete_my_account, name="delete_my_account"),
    path('teacher/view/student',views.teacher_view_student, name="teacher_view_student"),
    path('teacher/delete/student/<int:id>/', views.delete_student_by_teacher, name="delete_student_by_teacher"),
    path('teacher/profile/picture',views.update_teacher_profile_picture, name="update_teacher_profile_picture"),
    path('teacher/profile/update',views.update_teacher_details, name="update_teacher_details"),



]