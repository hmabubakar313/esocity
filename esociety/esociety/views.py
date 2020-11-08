from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls.static import static

def login(request):
    return render(request,"login.html")


def signup(request):
    return render(request,"signup.html")