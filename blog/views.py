from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = [“__all__”]
    success_url = reverse_lazy(“blog: all”)

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = “__all__”
    success_url = reverse_lazy(“blog: all”)


class PostDeleteView(UpdateView)
    model = Post
    fields = “__all__”
    success_url = reverse_lazy(“blog: all”)
