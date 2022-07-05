from distutils.command.upload import upload
from sqlite3 import Timestamp
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField #importar imagenes
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone


#Se instalo pillow

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

class Poster(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp= models.DateTimeField(default=timezone.now)
    content= RichTextField(blank=True, null=True)
    

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.nombre}: {self.content}'