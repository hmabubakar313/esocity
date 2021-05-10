from django.urls import path
from django.contrib import admin 
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from  django.conf.urls import  url
import blogpost
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('admin/login-user/', views.login,name='login'),
    path('admin/login-user/home/',views.home,name='home'),
    path('signup/',views.signup,name='admin/signup'),
    path('save/',views.save,name='admin/save'),
    path('list/',views.list,name='admin/users-list'),
    path('add-user/',views.add_user,name='admin/add-user'),
    path('save-user/',views.save_user,name='admin/save-user'),
    path('delete-user/<int:id>/',views.delete_user,name='admin/delete-user'),
    path('add-post/',views.add_post,name='admin/add-post' ),
    path('',include('blogpost.urls')),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



