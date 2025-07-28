from django.db import models
from django.contrib.auth.models import User

class User_Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='user/')


    def __str__(self):
        return self.user.username
    
    