str1=input('enter your string:')
res =(str1[::-1])
if res==str1:
    print(str1,'is palindrome')
else:
    print(str1,'not palindrome')


n = int(input('enter your number:'))
rev = 0
x = n
while (n > 0):
    rev = (rev * 10) + n % 10
    n = n // 10
if x == rev:
    print(rev, 'is palindrome')
else:
    print(rev, 'is not palindrome')


#armstrome num
num =int(input('enter your num: '))
def armstrm_num(num):
    order =len(str(num))
    sum=0
    original=num
    while num>0:
        digits =num%10
        sum+=digits**order
        num=num//10
    if sum==original:
        return True
    else:
        return False
if armstrm_num(num):
    print('armstrome')
else:
    print('not armstrome')

st1='suresh'
st2=''.join(reversed(st1))
print(st2)

test_str='aaabbbccc'
new_string=''
for i in range(len(test_str)):
    if i !=2:
        new_string=new_string+test_str[i]
print(new_string)










