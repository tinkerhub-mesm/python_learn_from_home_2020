from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog


#def index(request):
#    return HttpResponse("Hello, world. You're at the blog index.")


def index(request):
    blog = Blog.objects.all()
    argument={
        'name':'Pranay',
        'blog':blog
    }
    return render(request,'index.html',argument)

def slug(request,slug):
    blog = Blog.objects.filter(slug=slug)
    argument={
        'name':'Pranay',
        'blog':blog
    }
    return render(request,'blogtemplate.html',argument)

def dashboard(request):
    blog = Blog.objects.all()
    argument={
        'blog':blog
    }
    return render(request,'dashboard.html',argument)