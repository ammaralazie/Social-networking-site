from .models import *

def picture_function(request):
    if request.user.is_authenticated :
        profile=Profile.objects.get(user=request.user)
        return {'picture':profile.avatar}
    return {}

def receive_request_number(request):  
    if request.user.is_authenticated : 
        profile=Profile.objects.get(user=request.user)
        count=Relationship.objects.invatation_reccieved(profile)
        return {'invite_num':count.all().count()}
    return {}
    