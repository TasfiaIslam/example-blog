from django.http import HttpResponse
from django.shortcuts import redirect

# restrict authenticated users to view login, register pages 

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/posts/')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func