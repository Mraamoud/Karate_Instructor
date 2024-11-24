from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    subscribed = models.BooleanField(default=False)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)
    subscription_date_limit = models.DateTimeField(null=True)