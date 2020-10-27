from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
#from .mocks import Post
from .models import Post
from django.http import Http404
from .forms import PostForm
from django.contrib import messages

def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', {'posts': posts})

def show(request, id):
    post = get_object_or_404(Post, pk=id)
   
    # REMPLACE :

    # try:
    #     post = Post.objects.get(pk=id)
    # except:
    #     raise Http404('Sorry, post #{} not found.'.format(id))
    return render(request, 'blog/show.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) # instance du form
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('blog:index')
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


    post = get_object_or_404(Post, pk=id)
    messages.add_message(request, messages.INFO, 'Le post #{} a bien été supprimé.'.format(id))
    post.delete()
    return redirect('blog:index')


def post_upd(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save()
            post.save()
            #return redirect('blog:index')
            return redirect('blog:show', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_supp(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('blog:index')
