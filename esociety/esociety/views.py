from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls.static import static
import mysql.connector as mysql

# from .models import students
def save_login(request):

  

    # return render(request,"login.html")


def signup(request):
    return render(request,"signup.html")