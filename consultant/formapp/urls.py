from django.urls import path, include
from . import views
urlpatterns = [
    path('formapp', views.formapp, name='formapp'),
]
