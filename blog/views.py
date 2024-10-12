from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


class PostListView(ListView):
    model = Post 
    template_name = "home.html" 

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    template_name = "post_create.html"
    model = Post
    fields = ["title", "body", "author"] 
    success_url = reverse_lazy("post_list") 

class PostDeleteView(DeleteView):
    template_name = "post_delete.html"
    model = Post
    success_url = reverse_lazy("post_list") 

class PostUpdateView(UpdateView):
    template_name = "post_update.html"
    model = Post
    fields = ["title", "body"]
    success_url = reverse_lazy("post_list") 