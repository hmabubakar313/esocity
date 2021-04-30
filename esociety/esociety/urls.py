from django.urls import path
from django.contrib import admin 
from django.urls import path, include 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('login/', views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('save/',views.save,name='save'),
    path('home/',views.home,name='home'),
    path('list/',views.list,name='users-list'),
    path('add-user/',views.add_user,name='add-user'),
    path('save-user/',views.save_user,name='save-user'),
   path('delete-user/<int:id>/',views.delete_user,name='delete-user'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



