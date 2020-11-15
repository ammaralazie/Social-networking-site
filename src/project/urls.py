from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('profiles/',include('profiles.urls',namespace='profiles')),
    path('posts/',include('post.urls',namespace='post')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)