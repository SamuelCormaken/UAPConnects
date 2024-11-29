from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Club(models.Model):
    clubId=models.IntegerField()
    clubName=models.CharField(max_length=200,blank=True,null=True)
    members=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.clubName
    description=models.TextField(max_length=250,blank=True,null=True)


# class ClubMember(models.Model):
#     clubId=models.ForeignKey(Club,on_delete=models.CASCADE,blank=True,null=True)
#     user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)




class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)
    image= models.ImageField(upload_to='post_images/', blank=True, null=True)
    timestamp=models.DateField(default=now)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    contents=models.TextField(max_length=250,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self) -> str:
        return self.contents
    
class Resources(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    file_choice=(
        ('Class_note','Class_note'),
        ('Faculty_info','Faculty_info'),
        ('University_info','University_info'),
        ('Rules_regulations','Rules_regulations'),
        ('Custom','Custom')
    )
    file_type=models.CharField(max_length=300,choices=file_choice,blank=True,null=True)
    resource=models.CharField(max_length=200,blank=True,null=True)
    dateuploaded= models.DateTimeField(default=now)
    def __str__(self) -> str:
        return self.file_type

class Forum(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    time=models.DateField(default=now)
    title=models.CharField(max_length=250,blank=True,null=True)
    query=models.TextField(max_length=250,blank=True,null=True)