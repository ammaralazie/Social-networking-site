from django.urls import path
from .views import *
app_name='profiles'


urlpatterns=[
  
    path('myprofile/',myprofile,name='myprofile'),
    path('my_invites/',invatation_recieved_view,name='invatation_recieved_view'),
    path('all_profiles/',profile_list_view,name='profile_list_view'),
    path('invite_profile/',invite_profile_list,name='invite_profile_list'),
    path('send_request/',send_invatitions,name='send_invatitions'),
    path('delete_friends/',remove_friends,name='remove_friends'),
    path('accept_invation/',accept_inivtation,name='accept_inivtation'),
    path('reject_invatation/',reject_inivtation,name='reject_inivtation'),
    path('<slug:slug>/',detail,name='detail'),

]