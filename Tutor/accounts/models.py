from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django import forms
from PIL import Image

# Create your models here.
class Profile(models.Model):
    #one user can have one profile and one profile can have one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    bio = models.TextField(blank = True)
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawargs):
        super().save(*args, **kawargs)

        img = Image.open(self.image.path)   #getting image

        #resize image if grater than 300px
        if img.height > 300 or img.width >300:
            im_size = (300, 300)
            img.thumbnail(im_size)
            img.save(self.image.path)
    
