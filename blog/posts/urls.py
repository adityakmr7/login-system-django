from django.urls import path
from django.urls import path, include
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='posts-home'),

]
