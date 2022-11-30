from django.db import models


def user_directory_path(instance, filename):
    #this file will be uploaded to MEDIA_ROOT /user(id)/filename
    return f'user_{instance.user}/{filename}'


class FileUpload(models.Model):
    user = models.TextField(null=True)
    file_name = models.TextField(null=True)
    imgfile = models.ImageField(null=True, upload_to=user_directory_path, blank=True)

   # def __str__(self):
      #  return self.imgfile.filename()