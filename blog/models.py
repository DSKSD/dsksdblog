# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(null=False)
    photo = ImageField(upload_to='%Y/%m/%d', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    def get_thumb(self):
        im = get_thumbnail(self.photo, '200x200', crop='center', quality=99)
        return im.url # remember that sorl objects have url/width/height attributes
    

class Comment(models.Model):
    # related_name은 1:N의 관계에서 1의 모델이 N의 모델을 부를때 사용할 attribute
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text