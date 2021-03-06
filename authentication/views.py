from django.http import Http404
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm # Default user form
from django.contrib import messages # To show flash messages

from .decorators import unauthenticated_user 
from .forms import CreateUserForm

# LOGIN VIEW ENDPOINT

@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            # Check if user exists in database
            if user is not None:
                login(request, user)
                return redirect('/posts/')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'test_login.html', context)
       

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register_page(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')           
            messages.success(request, 'Account was created for '+username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'test_register.html', context)
        