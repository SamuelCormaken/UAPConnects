from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Club(models.Model):
    clubId=models.IntegerField()
    clubName=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.clubName



class User(models.Model):
    userId=models.IntegerField()
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.email
    
class ClubMember(models.Model):
    clubId=models.ForeignKey(Club,on_delete=models.CASCADE,blank=True,null=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)




class Post(models.Model):
    postId=models.IntegerField(blank=True,null=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_choice=(
        ('HomePost','HomePost'),
        ('ForumPost','ForumPost')
    )
    post=models.CharField(max_length=300,choices=post_choice,blank=True,null=True)
    media= models.ImageField(upload_to='post_images/', blank=True, null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

class Comment(models.Model):
    commentId=models.IntegerField(blank=True,null=True)
    postId=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    contents=models.TextField(max_length=250,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self) -> str:
        return self.contents
    
class Resources(models.Model):
    resourceID=models.IntegerField(blank=True,null=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    file_choice=(
        ('Class_note','Class_note'),
        ('Faculty_info','Faculty_info'),
        ('University_info','University_info'),
        ('Rules_regulations','Rules_regulations'),
        ('Custom','Custom')
    )
    file_type=models.CharField(max_length=300,choices=file_choice,blank=True,null=True)
    dateuploaded= models.DateTimeField(null=True, blank=True)
