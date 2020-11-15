from django.shortcuts import render ,redirect
from .models import *
from profiles.models import *
from .forms import *
from .utils import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required


#  هاي تعتبر الصفحة الرئيسية التي سوف تعرض كل المنشورات وما يتعلق بها
@login_required
def like_and_commint(request):
    qs=Post.objects.all()
    post_added=False
    profile=Profile.objects.get(user=request.user)
    if 'postButton' in request.POST:
        add_post=Add_Post(request.POST,request.FILES)
        print('files :',request.FILES)
        print('gfghf :',add_post.is_valid())
        if add_post.is_valid():
            instance=add_post.save(commit=False)
            instance.auther=profile
            instance.save()
            post_added=True
            return redirect('/posts/')

    else:
        add_post=Add_Post()
       
    

    if 'commintButton' in request.POST:
         add_commint=Add_Commint(request.POST)
         if add_commint.is_valid():
             instance=add_commint.save(commit=False)
             instance.user=profile
             instance.post=Post.objects.get(pk=request.POST.get('post_id'))
             instance.save()
             return redirect('/posts/')
        
    else:
        add_commint=Add_Commint()
    context={
        'qs':qs,
        'profile':profile,
        'f':add_post,
        'c':add_commint,
        'post_added':post_added
    }
    return render(request,'post/main.html',context)

@login_required
def like_unlike(request):
    user =request.user
    if request.method =='POST' :
        print('request :',request.body)
        data=json.loads(request.body )
        print('data : ',data)
        post_id=data['post']
        print('post : ',post_id)
        post_obj=Post.objects.get(pk=post_id)
        print('post_obj :',post_obj)
        profile=Profile.objects.get(user=user)
        if profile in post_obj.like.all():
            post_obj.like.remove(profile)
        else:
            post_obj.like.add(profile)
        like,created=Like.objects.get_or_create(user=profile,post_id=post_id)
        if  created == False:
            if like.value=='like':
                like.value='unlike'
            else:
                like.value='like'
        else:
            like.value='like'

        like.save()
        post_obj.save()
       
        data={

            'value':like.value,
            'likes':post_obj.like.all().count(),

        }
        return JsonResponse(data,safe=False)
    return redirect('post:like_and_commint')

@login_required
def deletpost(request,slug):
    if request.user.is_authenticated:
        post=Post.objects.get(slug=slug)
        post.delete()
        return redirect('/posts/')
    else:
        x=message(request)
        return render(request,'post/delete.html', {'x':x})
               

@login_required
def updatetpost(request,slug):
    x=None
    post=Post.objects.get(slug=slug)
    if request.user.is_authenticated :
        profile=Profile.objects.get(user=request.user)
        if request.method =='POST':
             post=Add_Post(request.POST,request.FILES,instance=post)
             if post.is_valid():
                 post.auther=profile
                 post.save()
                 return redirect('/posts/')
        else:
            post=Add_Post(instance=post)
    else:
        x=message(request)
    context={
        'x':x,
        'post':post
    }
    return render(request,'post/update.html', context)
def test(request):
    return JsonResponse('hellow',safe=False)





        
       