from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db.models import Q
from django.views.generic import CreateView
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User, Teacher, Student, UserProfileImage
from .forms import StudentSignUpForm, TeacherSignUpForm, UserProfileForm, StudentUpdateForm
from .decorators import student_required, teacher_required
# Create your views here.

def no_access(request):
    diction = {}
    return render(request, 'multiauth/no_access.html', context = diction)


def multiauth(request):
    diction = {}
    return render(request, 'multiauth/index.html', context=diction)


@login_required(login_url='multiauth_login')
@student_required
def multiauth_student(request):
    user = request.user
    allstudents = User.objects.filter(is_student=True)
    profilepictures = UserProfileImage.objects.all()

    profile = UserProfileImage.objects.filter(user=user)
    diction = {'user':user, 'allstudents':allstudents, 'profilepictures':profilepictures}
    if profile:
        profile = UserProfileImage.objects.get(user=user)
        diction = {'user':user, 'profile':profile, 'allstudents':allstudents, 'profilepictures':profilepictures}

    return render(request, 'multiauth/student.html', context=diction)


@login_required(login_url='multiauth_login')
@teacher_required
def multiauth_teacher(request):
    user = request.user
    profile = UserProfileImage.objects.filter(user=user)
    if profile:
        profile = UserProfileImage.objects.get(user=user)
        diction = {'user':user, 'profile':profile}
    else:
        diction = {'user':user}
    return render(request, 'multiauth/teacher.html', context=diction)

def multiauth_register_student(request):
    myform = StudentSignUpForm()
    if request.method == 'POST':
        myform = StudentSignUpForm(request.POST)
        if myform.is_valid():
            myform.save()
            user = myform.cleaned_data.get('username')
            messages.success(request, 'Account Created for '+ user)
            return redirect('multiauth_login')
    diction = {'myform':myform}
    return render(request, 'multiauth/stu_register.html', context=diction)


@login_required(login_url='multiauth_login')
@student_required
def update_student_profile_picture(request):
    user = request.user
    userimage  = UserProfileImage.objects.filter(user=user)
    if userimage:
        image = UserProfileImage.objects.get(user=user)
        if request.method=='POST':
            myform = UserProfileForm(request.POST, request.FILES, instance=image)
            if myform.is_valid():
                myform.save(commit=True)
                return redirect('multiauth_student')
    else:
        if request.method=='POST':
            myform = UserProfileForm(request.POST, request.FILES)
            if myform.is_valid():
                user = user 
                image = myform.cleaned_data.get('image')
                register = UserProfileImage(user = user, image=image)
                register.save()
                messages.success(request, user)
                return redirect('multiauth_student')


@login_required(login_url='multiauth_login')
@student_required
def update_student_details(request):
    user = request.user
    user = User.objects.get(username=user)
    student = user
    if request.method=='POST':
        myform = StudentUpdateForm(request.POST, instance=student)
        if myform.is_valid():
            myform.save(commit=True)
            return redirect('multiauth_student')



def multiauth_register_teacher(request):
    myform = TeacherSignUpForm()
    if request.method == 'POST':
        myform = TeacherSignUpForm(request.POST)
        if myform.is_valid():
            myform.save()
            user = myform.cleaned_data.get('username')
            messages.success(request, 'Account Created for '+ user)
            return redirect('multiauth_login')
    diction = {'myform':myform}
    return render(request, 'multiauth/teacher_register.html', context=diction)




def multiauth_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_what = False
        is_student =False
        is_teacher = False
        is_superuser = False
        is_what = User.objects.filter(username=username)
        if is_what:
            is_what = User.objects.get(username=username)
            is_student = is_what.is_student
            is_teacher = is_what.is_teacher
            is_superuser = is_what.is_superuser

        if is_student == True:
            user = authenticate(request, username=username, password=password, is_student=True)
            if user is not None:
                login(request, user)
                return redirect('multiauth_student')
            else:
                messages.info(request, 'Wrong username/password')
                return redirect('multiauth_login')
            
        elif is_teacher == True:
            user = authenticate(request, username=username, password=password, is_teacher=True)
            if user is not None:
                login(request, user)
                return redirect('multiauth_teacher')
            else:
                messages.info(request, 'Wrong username/password')
                return redirect('multiauth_login')

        elif is_superuser==True:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                messages.info(request, 'Wrong username/password')
                return redirect('multiauth_login')

        else:
            messages.info(request, 'Wrong username/password')
            return redirect('multiauth_login')


    diction = {}
    return render(request, 'multiauth/login.html', context=diction)




def multiauth_logout(request):
    logout(request)
    return redirect('multiauth_login')



@login_required(login_url='multiauth_login')
def delete_my_account(request):
    if request.method == 'POST':
        userdata = request.user.id
        del_id = User.objects.get(id=userdata)
        del_id.delete()
        logout(request)
        return redirect('multiauth')