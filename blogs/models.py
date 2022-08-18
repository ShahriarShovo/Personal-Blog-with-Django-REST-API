from django.db import models
from account.models import User

# Create your models here.


class Blogs(models.Model):
    admin=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog_name=models.CharField(max_length=150,null=True,blank=True)
    blog_title=models.CharField(max_length=150,null=True,blank=True)
    blog_image=models.ImageField(upload_to='blog_image',null=True,blank=True)
    blog_body=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.blog_name


