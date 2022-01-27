from django.shortcuts import render,redirect
from . models import Blog
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    blog = Blog.objects.all()
    context={'blogs':blog}
    return render(request,'home.html',context) 

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog_detail.html',context)


