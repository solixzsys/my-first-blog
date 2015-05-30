from django.shortcuts import redirect, render

def post_list(request):
    return render(request,"index.html",{})