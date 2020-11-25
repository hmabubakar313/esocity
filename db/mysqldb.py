import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='admin', host='localhost', database='esociety'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS STUDENT")

#Creating table as per requirement
sql ='''CREATE TABLE STUDENT(
   USERNAME DOUBLE NOT NULL,
   E_MAIL DOUBLE,
   PASSWORD CHAR(250),
   REG_NO DOUBLE
)'''
cursor.execute(sql)

#Closing the connection
conn.close()
# * insering into database
conn = mysql.connector.connect(
   user='root', password='admin', host='localhost', database='esociety')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO STUDENT(
   USERNAME,E_MAIL , PASSWORD, REG_NO,)
   VALUES ('admin', 'admin@admin.com', 'admin', 'abc-123',)"""

try:
   # Executing the SQL command
   cursor.execute(sql)
    #  Commit your changes in the database
   conn.commit()

except: 
     conn.rollback()
   # Rolling back in case of error
  

# Closing the connection
conn.close()