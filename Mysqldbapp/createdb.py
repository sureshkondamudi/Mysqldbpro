import MySQLdb
mydb =MySQLdb.connect(host='localhost',user ='root',password='root',database='Harshdb')
my_cursor =mydb.cursor()
my_cursor.execute('create table emp(name varchar(50),role varchar (50),loc varchar (50))')

for i in my_cursor:
    print(i)
