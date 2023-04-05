from django.db import models
from django.contrib.auth.models import User
# from froala_editor.fields import FroalaField
from .helpers import *
from django.contrib.auth.models import User

# Create your models here.


class Blog_Model(models.Model):
    title = models.CharField(max_length=200, unique=True)
    discription = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,null=True, blank=True, unique=True)
    image = models.FileField(null=True, upload_to='blog-images')
    # image = models.ImageField(null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog_Model, self).save(*args, **kwargs)

