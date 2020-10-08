from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

def index(request):
    myposts= Blogpost.objects.all()                         #pylint: disable = no-member
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]         #pylint: disable = no-member
    return render(request, 'blog/blogpost.html',{'post':post})

