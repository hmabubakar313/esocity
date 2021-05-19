from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
from django.shortcuts import redirect, render

# Create your views here.
def post(request):
    return render(request,"blogpost.html")

def profile(request):
    return render(request,"profile.html")
