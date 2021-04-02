#static variables and static method
class student:
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
    def msg(self):
        print(self.name+'',+self.marks)
s1=student('suresh',100)
print(s1.name)
print(s1.marks)
s1.msg()
s2=student('ram',90)
print(s2.name)
print(s2.marks)
s2.msg()

#class veriable and Class method
class student:
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
    def msg(self):
        print(self.name+'',+self.marks,'%')
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))

s1=student('suresh',100)

name ='suresh'
marks=60
#s4=student.get_per(name,marks)
print(s4)




