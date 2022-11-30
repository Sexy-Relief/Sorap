from django.contrib import admin

# Register your models here.
from .models import FileUpload

class FilesonAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(FileUpload, FilesonAdmin)