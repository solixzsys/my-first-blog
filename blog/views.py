from django.shortcuts import redirect, render, get_object_or_404
from blog.models import Post
from django.utils import timezone
def post_list(request):
    posts=Post.objects.filter(published_date__lt=timezone.now()).order_by("published_date")
    return render(request,"index.html",{ 'posts': posts })

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,"detail.html",{ 'post': post })