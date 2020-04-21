from django.shortcuts import render
from django.http import HttpResponse



#def index(request):
#    return HttpResponse("Hello, world. You're at the blog index.")


def index(request):
    argument={
        'name':'Pranay',
    }
    return render(request,'index.html',argument)
