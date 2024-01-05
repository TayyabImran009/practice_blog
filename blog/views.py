from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
# Create your views here.


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form, 'action': 'Create'})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context =  {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)

    
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form, 'action': 'Edit'})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')