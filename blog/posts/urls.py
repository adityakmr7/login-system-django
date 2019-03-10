from django.urls import path
from django.urls import path, include
from .views import PostView, PostDetailView, CategoryDetailView

urlpatterns = [
    path('', PostView.as_view(), name='posts-home'),
    path('<slug>', PostDetailView.as_view(), name='posts-detail'),
    path('category/<slug>', CategoryDetailView.as_view(), name='category-detail'),

]
