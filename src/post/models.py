from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile
from django.utils.text import slugify
import datetime
# Create your models here.
class Post (models.Model):
    content=models.TextField()
    image=models.ImageField(upload_to='posts',blank=True)
    like=models.ManyToManyField(Profile,blank=True,related_name='likes') 
    update=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)
    auther=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts')
    slug=models.SlugField(blank=True,null=True)

    def num_like(self):
        return self.like.all().count()

   

    def num_commintes(self):
        return self.commint_set.all().count()

     #here we use commint_set becuese i dont have any relationship from post to commint but i have in reverce.

    def __str__(self):
        return self.content[:20]

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(str(self.auther.slug)+str(datetime.datetime.now().timestamp()).replace('0','ammar'))
        super(Post,self).save(*args,**kwargs)
    

class Commint(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.CharField(max_length=300)
    update=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)
    
LIKE_CHOICES=(('like','like'),('unlike','unlike'))

class Like(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post')
    value=models.CharField(max_length=8,blank=True,choices=LIKE_CHOICES)
    update=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)+str(self.post)+str(self.value)