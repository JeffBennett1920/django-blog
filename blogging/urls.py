from django.urls import path
from blogging.views import list_view

from blogging.views import PostDetailView

urlpatterns = [
    path('', list_view, name="blog_index"),
    # path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]
