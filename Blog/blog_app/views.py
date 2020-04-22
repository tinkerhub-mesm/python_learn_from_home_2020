from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib import messages
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

def login(request):
    if request.method == 'POST':
         username = request.POST['userid']
         password = request.POST['password']
         user = auth.authenticate(username=username,password=password)
         if user is not None:
            auth.login(request,user)
            print("Loged in")
            return redirect("/dashboard")
         else:
            messages.error(request,'invalid')
            return redirect("/login")
    else:
      return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def add(request):
    if request.method == 'POST':
         title = request.POST['title']
         body = request.POST['body']
         slug = request.POST['slug']
         blog_add = Blog(title=title,body=body,slug=slug)
         blog_add.save() 
         return redirect("/dashboard")
    else:
      return render(request,'add.html')
    
def delete(request):
    if request.method == 'POST':
         blog_id = request.POST['id']
         Blog.objects.filter(id=blog_id).delete()
         return redirect("/dashboard")
    else:
      return render(request,'add.html')