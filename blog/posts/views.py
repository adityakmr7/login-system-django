from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.models import User
# Create your views here.posts = [
from django.shortcuts import redirect

#class based view
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Post.objects.all()[:10]
        else : 
            return super().get_queryset()


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'posts/post_detail.html'