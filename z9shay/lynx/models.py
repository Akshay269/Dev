from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True,default='Default.png')

    user=models.ForeignKey(User,on_delete=models.CASCADE,max_length=10)  