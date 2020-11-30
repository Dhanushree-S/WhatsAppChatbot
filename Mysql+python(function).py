import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="kavi",database="whatsapp_chatbot") 

print(mydb)

mycursor = mydb.cursor()

def createdb():
    mycursor.execute("CREATE DATABASE whatsapp_chatbot")

def showdb():
    mycursor.execute("Show databases;")
    for x in mycursor:
        print(x)

def createtable():
     mycursor.execute("CREATE TABLE (mobile_no varchar(20) PRIMARY KEY) ");

def describe():
    mycursor.execute("Describe user_info;")
    for x in mycursor:
        print(x)
        
def insert():
    sql = "INSERT INTO user_info (mobile_no) VALUES (%s)"
    val = ("9986242310")
    mycursor.execute(sql,(val,))
    mydb.commit() 
    print(mycursor.rowcount, "record inserted.")
    
def select():
    mycursor.execute("Select * from user_info;")
    for x in mycursor:
          print(x)
          
#createtable()
#describe()
insert()
select()


      
      





