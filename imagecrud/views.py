from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.db.models import Q
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ImageUploadForm
# Create your views here.


def imagecrud(request):
    allimage = ImageDatabase.objects.all()
    total_image = allimage.count()
    diction = {'allimage':allimage, 'total_image':total_image}
    if request.method=='POST':
        myform = ImageUploadForm(request.POST, request.FILES)
        
        if myform.is_valid():
            myform.save(commit=True)
            return HttpResponseRedirect('/imagecrud')

    return render(request, 'imagecrud/index.html', context=diction)




def imagecrud_delete_image(request, id):
    if request.method == 'POST':
        delete_id = ImageDatabase.objects.get(pk=id)
        delete_id.delete()
        messages.success(request, 'Image deleted successfully')
        return HttpResponseRedirect('/imagecrud')

def imagecrud_edit(request, id):
    img = ImageDatabase.objects.get(pk=id)
    diction = {'img':img}
    return render(request, 'imagecrud/edit_image.html', context=diction)


def crudimage_edit_delete_backup(request, id):
    img = ImageDatabase.objects.get(pk=id)
    string_id = str(id)
    if request.method=='POST':
        u_id = ImageDatabase.objects.get(pk=id)
        myform = ImageUploadForm(request.POST, request.FILES, instance=u_id)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Image updated successfully')
            return HttpResponseRedirect('/imagecrud/edit_image/'+string_id+'/')



def crudimage_update(request, id):
    img = ImageDatabase.objects.get(pk=id)
    string_id = str(id)
    if request.method=='POST':
        u_id = ImageDatabase.objects.get(pk=id)
        myform = ImageUploadForm(request.POST, request.FILES, instance=u_id)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Image updated successfully')
            return HttpResponseRedirect('/imagecrud/edit_image/'+string_id+'/')

