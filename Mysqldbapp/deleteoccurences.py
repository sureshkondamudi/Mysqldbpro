str1=['S1','S2','S3','S4','S5','S1','S2','S3']

emp=[]
for i in range(len(str1)):
    if i not in emp and i>2:

        emp.append(str1[i])
print(emp)

l='abcdabcdefghfgh'
ch=[]
for i in l:
    if i not in ch:
        ch.append(i)
ch=''.join(l)
print(ch)

# print duplicate elements
l2=[1,2,5,6,1,2]
empty_list=[]
count=0
for i in l2:
    for j in l2:
        if i==j:
            count=count+1
        if i not in empty_list and count>1:
            empty_list.append(i)
    count=0
print(empty_list)

str2=['S1','S2','S3','S4','S5','S1','S2','S3']
emptylist=[]
count1=0
for i in str2:
    for j in str2:
        if i==j:
            count1=count1+1
        if count1>1 and i not in emptylist:
            emptylist.append(i)
    count1=0
print(str2)
print(emptylist)

