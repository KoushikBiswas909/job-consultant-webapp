from django.contrib import admin
from .models import job_post

# Register your models here.
admin.site.register(job_post)


class job_post_Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file')
