from django import views
from django.contrib import admin
from django.urls import path, include
from mainapp import views
from mainapp.views import JobSearch

urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
    path('job_post/<int:pk>/', views.JobDetail.as_view(), name='jobpost'),
    path('job/search/', JobSearch.as_view(), name='job-search')
]
