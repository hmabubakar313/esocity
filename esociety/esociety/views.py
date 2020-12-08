from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls.static import static
import mysql.connector as mysql
import mysql.connector as mysql
# from .models import students
def login(request):
    return render(request,"login.html")
    # return render(request,"login.html")


def signup(request):
    return render(request,"signup.html")

def save_signup(request):
    if request.method=='POST':
    message_data = request.POST['message']        
    return render(request,"test.html")
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