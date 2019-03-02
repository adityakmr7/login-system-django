from django.shortcuts import render, get_object_or_404
#class based view
from django.views.generic import ListView, DetailView
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
#from django.contrib.auth.models import User
# Create your views here.posts = [

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
