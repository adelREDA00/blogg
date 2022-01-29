import profile
from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField(max_length=300,default="s1mple")
    profile_pic = models.ImageField(null=Tree , blank= True , upload_to = 'images/profile')
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=300)
    pic = models.ImageField(null=Tree , blank= True , upload_to = 'images/')
    title_tag = models.CharField(max_length=300,default="s1mple")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank = True , null= True )
    post_date=models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200,default='coding')
    likes = models.ManyToManyField(User,related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' +str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
