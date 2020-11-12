from django.urls import path
from . import views
from api.views import  UserList, UserLoginView


urlpatterns = [
    path('', views.index ),
    path('users/', UserList.as_view() ),
    path('login/', UserLoginView.as_view() ),
]