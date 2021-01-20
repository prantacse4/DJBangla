from django.shortcuts import render

# Create your views here.

def livecrudsearch(request):
    diction = {}
    return render(request, 'livecrudsearch/index.html', context = diction)