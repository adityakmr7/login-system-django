from django.urls import path
from django.urls import path, include
from .views import PostListView,PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='posts-detail'),
]
