from django.shortcuts import render, HttpResponseRedirect, redirect


def multiauth(request):
    diction = {}
    return render(request, 'multiauth/multiauth.html', context = diction)




