from turtle import title
from django.db import models

# Create your models here.


class job_post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
