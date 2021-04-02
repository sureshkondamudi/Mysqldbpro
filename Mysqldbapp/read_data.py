import MySQLdb
mydb =MySQLdb.connect(host='localhost',user ='root',password='root',database='Harshdb')
my_cursor =mydb.cursor()

my_cursor.execute('select * from emp')

my_result =my_cursor.fetchall()

for j in my_result:
    print(j)

mydb.commit()
