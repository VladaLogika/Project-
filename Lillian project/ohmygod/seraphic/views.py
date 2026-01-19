from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment

# Create your views here.

def home(request):

    all_posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': all_posts
    }
    return render(request, 'seraphic/home.html', context) 



def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk,published=True) #pk - айди статті
    post.views += 1
    post.save()

def about(request):
    return render(request, 'seraphic/aboutus.html')

def reviews(request):
    return render(request, 'seraphic/reviews.html')
    
def reviews(request):

    all_comments = Comment.objects.all().order_by('-created_at')
    context = {
        'comments': all_comments
    }
    return render(request, 'seraphic/reviews.html', context) 


    
