from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #one user can have one profile and one profile can have one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    bio = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'
    
