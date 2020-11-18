from django.shortcuts import render
from blog.models import Blog


def blog(request):

    posts = Blog.objects.order_by('-fecha')     

    return render(request, 'blog.html', {'posts' : posts})