from django.urls import path
from .views import PostCreateView

urlpatterns = [
    path("blog/", include("blog.urls", namespace="blog"))

]