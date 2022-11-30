from django.urls import path

from . import views

app_name='sorap'

urlpatterns = [
    path('', views.index,name='index'),
    path('main/',views.main,name='main'),
    path('fileupload/', views.fileUpload, name="fileupload"),
    path('filedelete/', views.fileDelete, name="filedelete"),
    path('filedownload/', views.fileDownload, name="filedownload"),

]