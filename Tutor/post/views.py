from django.shortcuts import render
from . models import Post

#dummy data
posts = [
    {
        'author': 'Corey',
        'title': 'Blog 1',
        'content': 'First post',
        'date': 'July 21 2022',
    },
    {
        'author': 'Jane',
        'title': 'Blog 2',
        'content': 'Second post',
        'date': 'July 21 2022',
    }
]

# Create your views here.
def home(request):
    context = {
        #'posts': posts,
        'posts': Post.objects.all(),
    }
    return render(request, 'post/home.html', context)
