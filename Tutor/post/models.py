from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #"on_delete" means if a user is del, post are del

    #this returns how you want the post to be printed, this case by title
    def __str__(self):
        return self.title

    #letting the view know where you want to redirect once you create a new post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})   #redirecting to detail page

    
