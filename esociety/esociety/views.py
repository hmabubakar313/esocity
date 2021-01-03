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
        try:
            conn = mysql.connector.connect(user='root', password='admin', host='localhost', database='esociety')
            cursor = conn.cursor()
            #Dropping EMPLOYEE table if already exists.
            cursor.execute("DROP TABLE IF EXISTS students")
            #Creating table as per requirement
            tableQuery = """CREATE TABLE students ( 
                                Id int(11) NOT NULL,
                                username varchar(250) NOT NULL,
                                e_mail varchar(255) NOT NULL,
                                password int(20) NOT NULL,
                                birthday Date NOT NULL,
                                reg_no varchar(255) NOT NULL,
                                PRIMARY KEY (Id)) """
            cursor = conn.cursor()
            cursor.execute(tableQuery)
            print("Laptop Table created successfully ")
            conn.close()
            conn = mysql.connector.connect(host='localhost',
                                                database='esociety',
                                                user='root',
                                                password='admin')
            cursor = conn.cursor()
        except mysql.connector.Error as error:
                    print("Failed to create table in MySQL: {}".format(error))
        finally:
            if (conn.is_connected()):
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='esociety',
                                         user='root',
                                         password='admin')
            inserQuery = """INSERT INTO students (Id,username,e_mail ,password, birthday, reg_no) 
            VALUES 
            (1, "username", "e_mail", password,"birthday","reg_no") """

            cursor = connection.cursor()
            cursor.execute(inserQuery)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()

        except mysql.connector.Error as error:
             print("Failed to insert record into Laptop table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return render(request,"test.html",{'person':person})

    else:
    # print(request.POST.get)
             return HttpResponse('<h1>Page  found</h1>')
