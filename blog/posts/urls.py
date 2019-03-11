from django.urls import path
from django.urls import path, include
from .views import PostView, PostDetailView,LatestPostView, CategoryPostListView

urlpatterns = [
    path('', PostView.as_view(), name='posts-home'),
    path('latest/', LatestPostView.as_view(), name='posts-latest'),
    path('<slug>', PostDetailView.as_view(), name='posts-detail'),
    path('category/<slug>', CategoryPostListView.as_view(), name='category-detail'),

]
