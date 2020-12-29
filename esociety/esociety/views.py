from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls.static import static
import mysql.connector as mysql
from django.shortcuts import redirect, render

# from .models import students
def login(request):
    return render(request,"login.html")
    # return render(request,"login.html")


def signup(request):
    # x=(request.GET.username)
    return render(request,"signup.html")

def save(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        birthday = request.POST['birthday']
        reg_no = request.POST['reg_no']
        person={
            'username':username,
            'password':password,
            'email':email,
            'birthday':birthday,
            'reg_no':reg_no,
        }
    if (username=='hmabubakar313'):
        return render(request,"test.html",{'person':person})
    else:
    # print(request.POST.get)
        return HttpResponse('<h1>Page  found</h1>')

"""  conn = mysql.connect(
   user='root', password='admin', host='localhost', database='esociety'
)
    print(conn)
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # *Dropping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS students")
    # Creating table as per requirement
    # #Closing the connection
    conn.close()
    #* insering into database
    # conn = mysql.connector.connect(
    # user='root', password='admin', host='localhost', database='esociety')
 """