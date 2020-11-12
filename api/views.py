from rest_framework import generics, permissions, mixins

from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, UserLoginSerializer
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserLoginSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

#Token API
class TokenApI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Get you token!'}
        return Response(content)

#Login API
class UserLoginView(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class UserList(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        content = {'message': 'Hello!'}
        return Response(content)

