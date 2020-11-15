from django.urls import path
from .views import *
app_name='accounts'

urlpatterns=[
    path('logout',logout_view,name='logout'),
]