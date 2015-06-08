from django.shortcuts import redirect, render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout

def post_list(request):
    posts=Post.objects.filter(published_date__lt=timezone.now()).order_by("-published_date")
    return render(request,"index.html",{ 'posts': posts })

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    #if post.published_date is not None:
    return render(request,"detail.html",{ 'post': post })
    #else:
    #    return redirect('blog.views.post_list')

@login_required
def post_new(request):
    if request.method=="POST":        
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()

            return redirect('blog.views.post_detail',pk=post.pk)
        else:
            form=PostForm()
        return render(request,'post_edit.html',{'form':form})
    else:
        form=PostForm()
        return render(request,'post_edit.html',{'form':form})

@login_required
def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
        return render(request,'post_edit.html',{'form':form})


def post_draft(request):
    posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,"index.html",{ 'posts': posts })

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return render(request,"detail.html",{ 'post': post })


@login_required
def post_remove(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect("/")


def mylogout(request):
    logout(request)
    return redirect("/")

def map(request):
    return render(request,"map.html",{})

def mapkml(request,mapf):
    #print (mapfile)
    return render(request,mapf,{})
    #redirect(mapf)