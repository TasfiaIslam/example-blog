from django.urls import path
from api.views import  RegisterApi, TokenApI, UserListCreate
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterApi.as_view(), name="register"),

    #JWT tokens
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    path('hello/', TokenApI.as_view() ),

    
]