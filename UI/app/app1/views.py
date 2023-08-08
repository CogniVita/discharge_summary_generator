from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyFileForm

from django.contrib import messages

# Create your views here.

def index(request):
    myform=MyFileForm()
    context={'form':myform}
    return render(request, 'index.html',context)
    




def base(request):
    return render(request, "app/base.html" )