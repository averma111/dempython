import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="dbconnection",passwd="root123",db="testdb");

if  mydb.is_connected():
    print("Connection Successfull");
else:
    print("Connection Failed");


mycur=mydb.cursor();

mycur.execute("use testdb");

mycur.execute("Insert into testdata values('123','root')");

mycur.execute("select * from testdata");

data=mycur.fetchall();

for cols in data:
    print(cols);

mycur.close();






