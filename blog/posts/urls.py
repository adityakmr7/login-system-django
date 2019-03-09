from django.urls import path
from django.urls import path, include
from .views import PostView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='posts-home'),
    path('<slug>', PostDetailView.as_view(), name='posts-detail'),
]
