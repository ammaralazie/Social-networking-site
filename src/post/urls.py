from django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name='post'

urlpatterns=[
    path('',like_and_commint,name='like_and_commint'),
    path('like/',like_unlike,name='like_unlike'),
    path('delete/',TemplateView.as_view(template_name='post/delete.html'),name='delete'),
    path('delete/<slug:slug>/',deletpost,name='deletpost'),
    path('update/<slug:slug>/',updatetpost,name='updatetpost'),
    path('test/',test,name='test'),
]
