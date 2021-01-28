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
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



