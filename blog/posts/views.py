from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.models import User
# Create your views here.posts = [
from django.shortcuts import redirect, render,get_object_or_404

#class based view
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostView(ListView):
   template_name = 'posts/home.html'
   model = Category
   context_object_name = 'all_categs'

   def get_queryset(self):
      if not self.request.user.is_authenticated:        
         return Category.objects.all()[0:6]
      else:
         return Category.objects.all()
   
   def get_context_data(self):
      context = super(PostView, self).get_context_data()
      context['latest_posts'] = Post.objects.order_by('-date_posted')[0:8]
      return context

   # def get_success_url(self):
   #     return reverse('home') #add your path


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'posts/post_detail.html'