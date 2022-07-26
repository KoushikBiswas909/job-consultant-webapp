from django.db import models

# Create your models here.


class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
