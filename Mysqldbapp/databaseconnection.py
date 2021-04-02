import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb
mydb =MySQLdb.connect(host='localhost',user ='root',password='root')
my_cursor =mydb.cursor()
my_cursor.execute('show databases')

for d in my_cursor:
    print(d)

s='suresh'
s1=s[0]
print(s1)

def outer(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
@outer
def decoratefun():
    return 'python developer'

obj =decoratefun()
print(decoratefun())


from collections import OrderedDict
#def remove_duplicate(str1):
 # return "".join(OrderedDict.fromkeys(str1))

#print(remove_duplicate("aaabbbccc"))
#print(remove_duplicate("w3resource"))
# delete duplicates in string
str1 ="aaabbbccc"
str2="".join(OrderedDict.fromkeys(str1))
print(str2)

l=[1,2,3,4,5,6,7,6,5,4,3,2]
new_list =[]
for i in l:
    if i not in new_list and i>1:
        new_list.append(i)
print(new_list)

l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

l=[1,2,3,4]
b=['a','b','c','d']
d=dict(zip(l,b))
print(d)


# Decorator
import time
def time_take(func):
    def inner(*args,**kwargs):
        start =time.time()
        result=func(*args,**kwargs)
        end =time.time()
        print(func.__name__+'took time'+str(end-start*1000)+'Msec')
        return result
    return inner
@time_take
def Squres(n):
    result=[]
    for i in n:
        result.append(i*i)
    return  result
@time_take
def Cubes(n):
    result  =[]
    for i in n:
        result.append(i*i*i)
    return result

arry  =range(1,10)
sqr =Squres(arry)
cub =Cubes(arry)
print(sqr)
print(cub)


#
def outer(f):
    def inner():
        result =f()
        return result.upper()
    return inner
@outer
def dfuntion():
    return 'python developer'

print(dfuntion())

#
def division(fun):
    def idivision(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return idivision
@division
def div(a,b):
    return a/b

div1=division(div)
print(div(2,8))

s='suresh'
s1=''.join(s)
print(reversed(s))


