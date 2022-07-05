from email.quoprimime import body_check
from pdb import post_mortem
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.shortcuts import render

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    image = models. ImageField(upload_to='blog/images')
    #date = models.DateField(datetime.date.today)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.user)

    #def get_absolute_url(self):
    #    return render(self, "posts.html") #, kwargs={'pk': self.pk}
    #    return reverse('/')
    #def get_absolute_url(self):

class Comments(models.Model):
    title= models.CharField(max_length=200)
    body= RichTextField(blank=True, null=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    add_time= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.post)