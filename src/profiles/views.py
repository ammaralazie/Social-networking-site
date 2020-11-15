from django.shortcuts import render,redirect
from .models import *
from .forms import UpdateProfile
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def myprofile(request):
    profile=Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form=UpdateProfile(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            check=True        
    else :
        form=UpdateProfile(instance=profile)
        check=False
       
    context={
        'profile':profile,
        'form':form,
        'check':check,
    }
    return render(request,'profile/myprofile.html',context)



@login_required
def invatation_recieved_view(request):
    profile=Profile.objects.get(user=request.user)
    qs=Relationship.objects.invatation_reccieved(profile)
    resulte=[]
    for x in qs :
        resulte.append(x.sender)

    context={
        'qs':resulte,
    }
    return render(request,'profile/invite.html',context)

@login_required
def accept_inivtation(request):
    if request.method=='POST':
        sender=Profile.objects.get(user=request.POST['profile_pk'])
        receiver=Profile.objects.get(user=request.user)
        try:
            rel=Relationship.objects.get(sender=sender,reciever=receiver)
            if rel.state == 'send':
                rel.state='accepted'
            rel.save()
            return redirect('profiles:invatation_recieved_view')
        except :
            return redirect('profiles:invatation_recieved_view')

@login_required
def reject_inivtation(request):
    if request.method=='POST':
        sender=Profile.objects.get(user=request.POST['profile_pk'])
        receiver=Profile.objects.get(user=request.user)
        try:
            rel=Relationship.objects.get(sender=sender,reciever=receiver)
            rel.delete()
            return redirect('profiles:invatation_recieved_view')
        except :
            return redirect('profiles:invatation_recieved_view')



@login_required
def profile_list_view(request):
    user=request.user
    qs=Profile.objects.get_all_profile(user)
    pl=Profile.objectss.profilelist(request.user)
    print('pl :',pl)
    
    print('qs :',qs)
    context={
        'qs':qs,
        'rel_sender':pl['rel_sender'],
        'rel_resecer':pl['rel_resecer'],
    }
    return render(request,'profile/profile_list.html',context)


@login_required
def invite_profile_list(request):
    user=request.user
    qs=Profile.objects.get_all_profile_to_invite(user)

    context={
        'qs':qs
    }
    return render(request,'profile/invite_profile_list.html',context)


@login_required
def send_invatitions(request):
        if request.method =='POST':
            reciver=Profile.objects.get(pk=request.POST['profile_pk'])
            sender=Profile.objects.get(user=request.user)
            rel=Relationship.objects.create(sender=sender,reciever=reciver,state='send')
            rel.save()
            return redirect(request.META['HTTP_REFERER'])
        return redirect('profiles:profile_list_view')

@login_required
def remove_friends(request):
    if request.method =='POST':
        reciver=Profile.objects.get(pk=request.POST['profile_pk'])
        sender=Profile.objects.get(user=request.user)
        rel=Relationship.objects.get(
            (Q(sender=sender)& Q(reciever=reciver))|
            (Q(sender=reciver)& Q(reciever=sender))
        )
        rel.delete()
        return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def detail(request,slug):
    detail=Profile.objects.get(slug=slug)
    pl=Profile.objectss.profilelist(detail.user)
    context={
        'obj':detail,
        'rel_sender':pl['rel_sender'],
        'rel_resecer':pl['rel_resecer'],
    }
    return render(request,'profile/detail.html',context)
