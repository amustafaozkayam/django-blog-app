from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='default.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"