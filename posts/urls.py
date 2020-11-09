from django.urls import path
from posts.views import posts, post_details

urlpatterns = [
    path('', posts),
    path('<str:pk>', post_details, name="post-detail")
]
