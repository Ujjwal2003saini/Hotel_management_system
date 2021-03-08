# IMPORT MYSQL CONNECTOR WITH PYTHON
import mysql.connector as mysqlt

# CONNECT PYTHON WITH MYSQL SERVER TO ENTER GIVEN INFORMATION
mydb = mysqlt.connect(host="localhost",user="root",password="root",database="Hotel_Management")


cursor = mydb.cursor()
##
##cursor.execute("CREATE DATABASE Hotel_Management")

##create_table_1 = "CREATE TABLE Booking_info(SERIAL_NO int not null auto_increment,NAME varchar(30),AGE varchar(15),GENDER varchar(10),AADHAAR varchar(14),ADDRESS varchar(30),MOBILE varchar(15),NUMBER_ROOMS varchar(10),ROOM_RENT varchar(30),ROOM_TYPE varchar(5),ROOM_NUMBER varchar(10),primary key(SERIAL_NO))"
##cursor.execute(create_table_1)

##columns_create_1 ="INSERT INTO Booking_info(NAME,AGE,GENDER,AADHAAR,ADDRESS,MOBILE,NUMBER_ROOMS,ROOM_RENT,ROOM_TYPE,ROOM_NUMBER) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
##a=input("name = ")
##b=input("age = ")
##c=input("gender = ")
##d=input("aadhaar = ")
##e=input("address = ")
##f=input("mobi = ")
##g=input("number = ")
##h=input("rent = ")
##i=input("type = ")
##j=input("room number = ")
##
##_input_1 = (a,b,c,d,e,f,g,h,i,j)
##cursor.execute(columns_create_1,_input_1)
##mydb.commit()


##create_table_2 = "CREATE TABLE Booked_dates(SERIAL_NO int not null auto_increment,CHECK_IN_DATE varchar(5),CHECK_IN_MONTH varchar(5),CHECK_IN_YEAR varchar(5),CHECK_OUT_DATE varchar(5),CHECK_OUT_MONTH varchar(5),CHECK_OUT_YEAR varchar(5),primary key(SERIAL_NO))"
##cursor.execute(create_table_2)

##columns_create_2 ="INSERT INTO Booked_dates(CHECK_IN_DATE,CHECK_IN_MONTH,CHECK_IN_YEAR,CHECK_OUT_DATE,CHECK_OUT_MONTH,CHECK_OUT_YEAR) VALUES(%s,%s,%s,%s,%s,%s)"
##aa=input("DATE 1 = ")
##bb=input("MONTH 1 = ")
##cc=input("YEAR 1 = ")
##dd=input("DATE 2 = ")
##ee=input("MONTH 2 = ")
##ff=input("YEAR 2 = ")
##
##_input_2 = (aa,bb,cc,dd,ee,ff)
##cursor.execute(columns_create_2,_input_2)
##mydb.commit()

##create_table_3 = "CREATE TABLE adult_looping(SERIAL_NO int not null auto_increment,NAME varchar(30),AGE varchar(10),GENDER varchar(10),AADHAAR varchar(14),primary key(SERIAL_NO))"
##cursor.execute(create_table_3)

##columns_create_3 ="INSERT INTO adult_looping(NAME,AGE,GENDER,AADHAAR) VALUES(%s,%s,%s,%s)"
##aa=input("DATE 1 = ")
##bb=input("MONTH 1 = ")
##cc=input("YEAR 1 = ")
##dd=input("DATE 2 = ")
##
##_input_3 = (aa,bb,cc,dd)
##cursor.execute(columns_create_3,_input_3)
##mydb.commit()

mydb.close()
