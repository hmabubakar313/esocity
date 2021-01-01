from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls.static import static
import mysql.connector as mysql
from django.shortcuts import redirect, render
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

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
        e_mail = request.POST['email']
        birthday = request.POST['birthday']
        reg_no = request.POST['reg_no']
        person={
            'username':username,
            'password':password,
            'email':e_mail,
            'birthday':birthday,
            'reg_no':reg_no,
        }
    if (username=='hmabubakar313'):
        return render(request,"test.html",{'person':person})
        conn = mysql.connector.connect(user='root', password='admin', host='localhost', database='esociety')
        cursor = conn.cursor()
        #Dropping EMPLOYEE table if already exists.
        cursor.execute("DROP TABLE IF EXISTS STUDENT")
        #Creating table as per requirement
        conn.execute("CREATE TABLE students(username VARCHAR(255),email  VARCHAR(255),password  VARCHAR(255),reg_no  VARCHAR(255))")
        conn.close()
        conn = mysql.connector.connect(host='localhost',
                                            database='esociety',
                                            user='root',
                                            password='admin')
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                            VALUES 
                            (username, e_mail,password,birthday,reg_no) """

        cursor = conn.cursor()
        cursor.execute(mySql_insert_query)
        conn.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()
    # except mysql.connector.Error as error:
    #     print("Failed to insert record into Laptop table {}".format(error))

    # finally:
    #     if (conn.is_connected()):
    #         conn.close()
    #         print("MySQL connection is closed")
    else:
    # print(request.POST.get)
             return HttpResponse('<h1>Page  found</h1>')
# try:
    # cursor = conn.cursor()
   
   
#