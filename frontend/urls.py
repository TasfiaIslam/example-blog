from django.urls import path
from . import views
from api.views import  UserList


urlpatterns = [
    path('', views.index ),
    path('users/', UserList.as_view() ),
]