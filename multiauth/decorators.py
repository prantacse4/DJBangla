from django.shortcuts import render, HttpResponseRedirect, redirect

def student_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if True == user.is_superuser:
            return function(request, *args, **kwargs)
        elif True != user.is_student:
            return redirect('no_access')
        else:
            return function(request, *args, **kwargs)
    return wrapper


def teacher_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if True == user.is_superuser:
            return function(request, *args, **kwargs)
        elif True != user.is_teacher:
            return redirect('no_access')
        else:
            return function(request, *args, **kwargs)
    return wrapper
