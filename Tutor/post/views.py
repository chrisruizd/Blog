from django.shortcuts import render
from django.urls import reverse_lazy
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'post/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #setting the author of the post equal to the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #setting the author of the post equal to the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #users can only update posts if they are the author
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')  #redirect to home after delete a post

    #users can delete post only if they are the authors
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
            
    
    