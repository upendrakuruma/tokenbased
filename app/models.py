from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author',null=True,blank=True)

    def __str__(self):
        return self.title
    