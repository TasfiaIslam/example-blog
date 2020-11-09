from django.shortcuts import render

from django.contrib.auth.decorators import login_required # authenticate login


# POSTS VIEW ENDPOINT

@login_required(login_url='login')
def posts(request):
    return render(request, 'blog-listing.html')


# POST DETAILS VIEW ENDPOINT

@login_required(login_url='login')
def post_details(request):
    return render(request, 'blog-post.html')