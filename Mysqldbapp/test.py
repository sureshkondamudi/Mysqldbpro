class Insert:
    legs=6
    def __str__(self):
        legs=4
        return legs
    def __init__(self):
        self.legs=8
i=Insert()
print(i.legs)

#
import datetime as dt
from datetime import timedelta
format ='%A,%d-%B-%Y'
req_date =(dt.datetime.now()-timedelta(8)).strftime(format)
print('req date is: {}'.format(req_date))

#
def number(x):
    def sub(y):
        print(x-y)
    return sub
result =number(80)
result(50)

result =number(40)
result(70)
result=number(50)
result(80)
result=number(100)
result(80)


#
import re
p=re.compile('[a-t]+')
m=p.match('cats and dogs')
print(m.group())
#
with open('readword.txt','r') as f1:
    for line in f1:
        for word in line.split():
            print(word)


with open('readword.txt','r') as file:
    while True:
        rfile=file.read(3)
        if not rfile:
            break
        print(rfile)
# count no of char
with open('readword.txt','r') as file1:
    count=0
    content =file1.read()
    for ncount in content:
        if ncount:
            count+=1
    print(count)

#
lst =[2,3,4,5,6,7,8]
for i in lst:
    if i%2==0:
        print(i,end='')

count_list=0
for i in lst:
    count_list=count_list+1
print(count_list)
# to find sum of elements
lst2=[4,5,6]
total=0
for i in range(len(lst2)):
    total=total+lst2[i]
    print(total)

def max_ele(lst,n):
    max1=0
    final_list=[]
    for i in range(0,n):
        for j in range(len(lst)):
            if max1>lst[j]:
                final_list.append(max1)
        print(final_list)
#lst=max_ele([2,3,4,5])


with open('readword.txt','r') as ff:
    c=0
    for i in ff:
        for nchar in j:
            c+=1
    print(c)

s='sureshkonda'
if s in 'suresh':
    print(s)







