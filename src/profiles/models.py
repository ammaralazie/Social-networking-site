from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .utils import get_random_code
from django.db.models import Q

class profileListView(models.Manager):
    def profilelist(self,instance):
        user=User.objects.get(username__iexact=instance)
        profile=Profile.objects.get(user=user)
        rel_r=Relationship.objects.filter(sender=profile)
        rel_s=Relationship.objects.filter(reciever=profile)

        rel_resecer=[]
        for item in rel_r:
            rel_resecer.append(item.reciever.user)
        rel_sender=[]
        for item in rel_s:
            rel_sender.append(item.sender.user)

        posts=[]
        if len(profile.num_auther_post())>0 :
            posts=profile.num_auther_post
            check_post=True
            print('posts(:',posts)
        else:
            check_post=False
        print('check(:',check_post)

        
        context={'rel_sender':rel_sender,'rel_resecer':rel_resecer,'check_post':check_post,'posts':posts}
        return context

class ProfileManager(models.Manager):
   
    def get_all_profile(self,me):
        profiles=Profile.objects.all().exclude(user=me)
        return profiles


    def get_all_profile_to_invite(self,sender):
        profiles=Profile.objects.all().exclude(user=sender)
        profile=Profile.objects.get(user=sender)
        qs=Relationship.objects.filter(Q(sender=profile)| Q(reciever=profile))

        accepted=[]
        for rel in qs :
            if rel.state =='accepted':
                accepted.append(rel.sender)
                accepted.append(rel.reciever)
        print('accepted :',accepted)

        avalible=[]
        for pro in profiles :
            if not pro in accepted :
                avalible.append(pro)
        print(avalible)

        return avalible

class Profile(models.Model):
    firstname=models.CharField(max_length=300,blank=True)
    lastname=models.CharField(max_length=300,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(default='No bio ..',max_length=300)
    country=models.CharField(max_length=300,blank=True)
    avatar=models.ImageField(default='avatar.jpg',upload_to='avatar/')
    friends=models.ManyToManyField(User,blank=True,related_name='friends')
    slug=models.SlugField(unique=True,blank=True)
    update=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    objects=ProfileManager()
    objectss=profileListView()

    def number_of_freinds(self):
        return self.friends.count()
    def of_freinds(self):
        return self.friends.all()

    def num_post(self):
        return self.posts.all().count()


    def num_auther_post(self):
        return self.posts.all()

    def get_like_given_num(self):
        get_like=self.like_set.all()
        total=0
        for i in get_like:
            if i.value=='like':
                total +=1
        return total

    def get_like_recive_num(self):
        get_like=self.likes.all()
        total=0
        for i in get_like:
            total+=i.like.all().count()
        return total

    def __str__(self):
        return str(self.user)+"  "+str(self.created)

    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug=slugify(get_random_code())
        super(Profile,self).save(*args,**kwargs)


STATE_CHOICES=(('send','send'),('accepted','accepted'))

class RelationshipManager(models.Manager):
    def invatation_reccieved(self,reciever):
        qs=Relationship.objects.filter(reciever=reciever,state='send')
        return qs


class Relationship(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    reciever=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='reciever')
    state=models.CharField(max_length=8,choices=STATE_CHOICES)
    update=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    objects=RelationshipManager()

    def __str__(self):
        return str(self.sender)+"  "+str(self.reciever)+ " "+str(self.state)
