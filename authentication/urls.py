from django.urls import path
from authentication.views import login_page, register_page, logoutUser

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', register_page, name="register"),
]
