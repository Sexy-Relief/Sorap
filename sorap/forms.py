from django.forms import ModelForm
from .models import FileUpload

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['user','file_name','imgfile',]