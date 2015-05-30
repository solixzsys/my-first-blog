from django.shortcuts import redirect, render
from blog.models import Post
from django.utils import timezone
def post_list(request):
    posts=Post.objects.filter(created_date__lt=timezone.now())
    return render(request,"index.html",{ 'posts': posts })