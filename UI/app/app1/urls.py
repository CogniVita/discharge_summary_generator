from django.urls import path
from django.contrib import admin
from UploadFiles import views
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    
    path("base.html",views.base, name="base"),
    
]

