from django.shortcuts import render

# Create your views here.
def blogpost(request):
    return render(request,"blogpost.html")