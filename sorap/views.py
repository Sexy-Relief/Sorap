from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from .forms import FileUploadForm
from .models import FileUpload
from config import settings
import os
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'sorap/index.html')


def main(request):
    file_list=FileUpload.objects.filter(user=request.user.username)
    context = {'file_list': file_list}
    return render(request,'sorap/main.html',context)


def fileUpload(request):
    if request.method == 'POST':
        userinfo = request.POST["userinfo"]
        img = request.FILES["imgfile"]
        fname = img.name
        fileupload = FileUpload(
            user=userinfo,
            file_name=fname,
            imgfile=img,
        )
        fileupload.save()
        return redirect('sorap:main')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'sorap/fileupload.html', context)


def fileDelete(request):
    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        for item in selected:
            FileUpload.objects.filter(file_name=item).delete()
            thepath="user_"+request.user.username+"/"+item
            os.remove(os.path.join(settings.MEDIA_ROOT,thepath))
        return redirect('sorap:main')
    else:
        file_list = FileUpload.objects.filter(user=request.user.username)
        context = {'file_list': file_list}
        return render(request, 'sorap/filedelete.html', context)


def fileDownload(request):
    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        for item in selected:
            thepath = "user_" + request.user.username + "/" + item
            file_path = os.path.join(settings.MEDIA_ROOT,thepath)
            binary_file = open(file_path, 'rb')
            response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        #return redirect('sorap:main')
    else:
        file_list = FileUpload.objects.filter(user=request.user.username)
        context = {'file_list': file_list}
        return render(request, 'sorap/filedownload.html', context)