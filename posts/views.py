from django.shortcuts import render
from .models import Post
import json # to work with json file
import requests # to work with web url
from random import choice    
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required # authenticate login

# POSTS VIEW ENDPOINT

@login_required(login_url='login')
def posts(request):
 
    with open('posts.json') as f:        
        posts_json = json.load(f)    
        ids = [d.id for d in User.objects.all()]    
    
    for post in posts_json:        
        Post(title=post['title'], body=post['body'], author_id=choice(ids)).save()
    
    context = {'posts': Post.objects.all()}
        
    return render(request, 'blog-listing.html', context)


# POST DETAILS VIEW ENDPOINT

@login_required(login_url='login')
def post_details(request, pk):

    post_url = "https://jsonplaceholder.typicode.com/posts/"+pk
    post_response = requests.get(post_url).json()

    comment_url = post_url+"/comments"
    comment_response = requests.get(comment_url).json()

    context = {'post_response':post_response, 'comment_response':comment_response}
    return render(request, 'blog-post.html', context)