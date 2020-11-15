from django.contrib import messages
from django.contrib.messages import get_messages
def message(request):
    messages.warning(request,'plase login and try in another time ادعبل يلااااااااه')
    x=get_messages(request)
    if x :
        for x in x: 
            x=x
    return x