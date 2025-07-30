from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class User_Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='user/')


    def __str__(self):
        return self.user.username
    
    
class User_content(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50,verbose_name='title')
    content = models.TextField(verbose_name='content')
    content_image = models.ImageField(upload_to='user/content/images',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user_post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f' {self.user.username} | '
 