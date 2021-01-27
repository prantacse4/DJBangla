from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import StudentRegistration
from .forms import ProjectRegistration
from .forms import ProjectRegistrationRemoved

from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def crudsearch(request):
    # project = Project.objects.all()
    #Check Removed or Not
    project = Project.objects.filter(project_status=0)
    student = Student.objects.all()
    # PAGINATION_START
    pro_paginator = Paginator(project, 6) # Show 6 Projects per page
    pro_page = request.GET.get('page')
    try:
        project = pro_paginator.page(pro_page)
    except PageNotAnInteger:
        project = pro_paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        project = pro_paginator.page(pro_paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.
    # PAGINATION_END


    #HomePageAddProject
    if request.method == 'POST':
        myform = ProjectRegistration(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Project Created successfully')
            return HttpResponseRedirect('/crudsearch')
    else:
        myform = ProjectRegistration()



    removed_project_count = Project.objects.filter(project_status=1).count()
    active_project_count = Project.objects.filter(project_status=0).count()
    activeprojects = 2
    if active_project_count == 0:
        if removed_project_count == 0:
            activeprojects = 0
        else:
            activeprojects = 1

    total_projects = 0
    total_projects = Project.objects.all().count()
    diction = {'myform':myform, 'student':student, 'project':project, 'activeprojects':activeprojects, 'total_projects':total_projects}
    return render(request, 'crudsearch/index.html', context = diction)


        

def crudsearch_student(request):
    student = Student.objects.all()
    # PAGINATION_START
    stu_paginator = Paginator(student, 6)
    stu_page = request.GET.get('stu_page')
    try:
        student = stu_paginator.page(stu_page)
    except PageNotAnInteger:
        student = stu_paginator.page(1)
    except EmptyPage:
        student = stu_paginator.page(stu_paginator.num_pages)
    # PAGINATION_END


    #AddStudent
    if request.method == 'POST':
        myform = StudentRegistration(request.POST)
        if myform.is_valid():
            name = myform.cleaned_data['name']
            student_id = myform.cleaned_data['student_id']
            phone = myform.cleaned_data['phone']
            register = Student(name = name, student_id = student_id, phone = phone)
            register.save()
            messages.success(request, 'Student Added successfully')
            return HttpResponseRedirect('/crudsearch/student/')
    else:
        myform = StudentRegistration()

    diction = {'myform':myform, 'student':student}
    return render(request, 'crudsearch/student.html', context = diction)



def crudsearch_add_student(request):
    if request.method == 'POST':
        myform = StudentRegistration(request.POST)
        if myform.is_valid():
            name = myform.cleaned_data['name']
            student_id = myform.cleaned_data['student_id']
            phone = myform.cleaned_data['phone']
            register = Student(name = name, student_id = student_id, phone = phone)
            register.save()
            return HttpResponseRedirect('/crudsearch/student/')
        return HttpResponseRedirect('/crudsearch')
        


def crudsearch_delete_project(request, id):
    if request.method == 'POST':
        delete_id = Project.objects.get(pk=id)
        delete_id.delete()
        messages.success(request, 'Project deleted successfully')
        return HttpResponseRedirect('/crudsearch')


def crudsearch_delete_student(request, id):
    if request.method == 'POST':
        delete_id = Student.objects.get(pk=id)
        delete_id.delete()
        messages.success(request, 'Student deleted successfully')
        return HttpResponseRedirect('/crudsearch/student')


def crudsearch_remove_project(request, id):
    if request.method == 'POST':
        removed_id = Project.objects.get(pk=id)
        myform = ProjectRegistrationRemoved(request.POST, instance = removed_id)
        if myform.is_valid():
            project_status = myform.cleaned_data['project_status']
            if project_status == 1:
                myform.project_status = 1
                myform.save(commit=True)
                return HttpResponseRedirect('/crudsearch')
            elif project_status==0:
                myform.project_status = 0
                myform.save(commit=True)
                return HttpResponseRedirect('/crudsearch/crudsearch_removed/')




def crudsearch_removed(request):
    project = Project.objects.filter(project_status=1)

    # PAGINATION_START
    pro_paginator = Paginator(project, 6) # Show 6 Projects per page
    pro_page = request.GET.get('page')
    try:
        project = pro_paginator.page(pro_page)
    except PageNotAnInteger:
        project = pro_paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        project = pro_paginator.page(pro_paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.
    # PAGINATION_END

    removed_project_count = Project.objects.filter(project_status=1).count()
    active_project_count = Project.objects.filter(project_status=0).count()
    total_projects = 0
    total_projects = Project.objects.all().count()
    
    activeprojects = 2
    if removed_project_count == 0:
        if active_project_count == 0:
            activeprojects = 0
        else:
            activeprojects = 1
    diction = {'project':project, 'activeprojects':activeprojects, 'total_projects':total_projects}
    return render(request,  'crudsearch/removed_project.html', context = diction)



def crudsearch_removed_delete_project(request, id):
    if request.method == 'POST':
        delete_id = Project.objects.get(pk=id)
        delete_id.delete()
        messages.success(request, 'Project deleted successfully')
        return HttpResponseRedirect('/crudsearch/crudsearch_removed/')
