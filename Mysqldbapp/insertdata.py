import MySQLdb
mydb =MySQLdb.connect(host='localhost',user ='root',password='root',database='Harshdb')
my_cursor =mydb.cursor()

query_set ='insert into emp(name,role,loc) values (%s,%s,%s)'

employes =[('suresh','python','hyd'),('nani','java','chennai'),('ram','php','bangalore')]

my_cursor.executemany(query_set,employes)
mydb.commit()
