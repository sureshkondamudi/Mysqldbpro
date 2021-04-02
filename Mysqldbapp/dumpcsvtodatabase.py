import pymysql
import csv
import MySQLdb
import pandas as pd
pymysql.install_as_MySQLdb()


mydb =MySQLdb.connect(host='localhost',user ='root',password='root',database='Harshdb')

with open('C:\\Users\\91879\\Desktop\\file1.csv') as csv_file:
    csvfile =pd.read_csv(csv_file)
    allvalues =[]
    for row in csvfile:
        values =(row[0],row[1],row[2])
        allvalues.append(values)

quarys ='insert into empdetails(NAME,LOCATION,EMAIL),values(%s,%s,%s)'
my_cursor =mydb.cursor()
my_cursor.executemany(quarys,allvalues)
mydb.commit()





