from django.shortcuts import render, get_object_or_404
from .models import News
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
 

def post_list(request):
    posts=News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'news':posts})
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'news':post})
def post_new(request):
    if request.method == "News":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def catalog(request):
    return render(request,'blog/katalog.html',{})
# Create your views here.
