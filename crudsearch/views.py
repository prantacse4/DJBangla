from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import StudentRegistration
from .forms import ProjectRegistration


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def crudsearch(request):
    project = Project.objects.all()
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
    diction = {'student':student, 'project':project}
    return render(request, 'crudsearch/index.html', context = diction)


def crudsearch_add_project(request):
    if request.method == 'POST':
        myform = ProjectRegistration(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
            return HttpResponseRedirect('/crudsearch')
        return HttpResponseRedirect('/crudsearch')
        

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
    diction = {'student':student}
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
        