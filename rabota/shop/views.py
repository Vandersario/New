from django.shortcuts import render, get_object_or_404
from .models import News
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
 

def mainn(request):
    return render(request,'blog/main.html',{})
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'news':post})

