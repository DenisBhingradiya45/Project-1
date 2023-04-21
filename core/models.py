from django.db import models
from django.contrib.auth.models import User
from .helpers import *
from django.contrib.auth.models import User

# Create your models here.


class Blog_Model(models.Model):
    title = models.CharField(max_length=200, unique=True)
    discription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(null=True, upload_to='blog-images')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
    
