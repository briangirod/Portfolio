from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm, PostForm
from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostList(ListView):
    model= Post
    template_name= 'posts.html'
    ordering= ['-date']

#def render_posts(request):
#    posts = Post.objects.all()
#    return render(request, 'posts.html', {'posts': posts})
#

class VerPost(DetailView):
    model= Post
    template_name= 'post_detail.html'
#def post_detail(request, post_id):
#    post = get_object_or_404(Post, pk=post_id)
#    return render(request, 'post_detail.html', {"post": post})

class CrearPost(CreateView):
    model=Post
    form_class=PostForm
    template_name= 'crear_post.html'
    

@login_required
def addComment(request, pk):
    post= get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        my_form = CommentForm(request.POST)

        if my_form.is_valid():
            comment= my_form.save(commit=False)
            comment.author= request.user
            comment.post= post
            comment.save()
            #return HttpResponseRedirect()
            #def get_success_url(self, reverse):
                #return reverse('post_detail', id=post.pk)
            return redirect('post_detail', pk=post.pk)
        else:
            return HTTPResponse(f'Mal')
    else:
        my_form= CommentForm()

    return render(request, 'addComment.html', {'my_form': my_form})