from django.urls import path
from django.contrib import admin 
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from  django.conf.urls import  url
admin.autodiscover()

urlpatterns = [
     path('admin/', admin.site.urls), 
    path('admin/login/', views.login,name='login'),
    path('admin/signup/',views.signup,name='signup'),
    path('admin/save/',views.save,name='save'),
    path('admin/home/',views.home,name='home'),
    path('admin/list/',views.list,name='users-list'),
    path('admin/add-user/',views.add_user,name='add-user'),
    path('admin/save-user/',views.save_user,name='save-user'),
    path('admin/delete-user/<int:id>/',views.delete_user,name='delete-user'),
    path('admin/add-post/',views.add_post,name='add-post' ),
    url(r'^blogpost',include('blogpost.urls')),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



