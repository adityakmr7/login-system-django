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
      if self.request.user.is_authenticated:        
         return Category.objects.all()
      else:
         return Category.objects.all().exclude(title__iexact = 'Featured')[:6]
   
   def get_context_data(self):
      if not self.request.user.is_authenticated:   
         fcategory = Category.objects.get(title__iexact = 'Featured')        
         context = super(PostView, self).get_context_data()
         context['latest_posts'] = Post.objects.order_by('-date_posted')[0:6]
         context['featured_posts'] = Post.objects.all().filter(category= fcategory).order_by('-date_posted')[0:6]
         return context
      else:
         fcategory = Category.objects.get(title__iexact = 'Featured') 
         context = super(PostView, self).get_context_data()
         context['latest_posts'] = Post.objects.order_by('-date_posted')
         context['featured_posts'] = Post.objects.all().filter(category= fcategory).order_by('-date_posted')[0:6]
         return context
         
   # def get_success_url(self):
   #     return reverse('home') #add your path


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

   

class CategoryDetailView(LoginRequiredMixin, DetailView):
   model = Category
   template_name = 'posts/category_detail.html'

   # def get_context_data(self):
   #    context = super(PostView, self).get_context_data()
   #    context['posts'] = Post.objects.order_by('-date_posted')
   #    return context