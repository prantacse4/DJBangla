from django.shortcuts import render
# Create your views here.


def starter(request):
    diction = {}
    return render(request, 'basics/starter.html', context = diction)