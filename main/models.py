from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class New(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    banner_image = models.ImageField(upload_to='news/banner_images')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def images(self):
        return NewImage.objects.filter(new=self)

    @property
    def videos(self):
        return NewVideo.objects.filter(new=self)


class NewImage(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/images')


class NewVideo(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    video = models.FileField(upload_to='news/videos', null=True, blank=True)
    url = models.URLField(null=True, blank=True)


class Comment(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)




