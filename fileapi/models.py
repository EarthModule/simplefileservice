from django.db import models

# Create your models here.
class FileModel(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
