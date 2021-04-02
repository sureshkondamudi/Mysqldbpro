class Computer():
    __price=100
    def setprice(self):
        print('current price is :',self.__price)
    def updateprice(self,price):
        self.__price=price


obj =Computer()
obj.setprice()
obj.updateprice=1000
print('updated price is:',obj.updateprice)

#MRO
class A:
    def process(self):
        print('A process')
class B:
    def process(self):
        print('B process')
class C(A,B):
    pass

class D(C,B):
    pass

obj =C()
obj.process()

#multiple inheritance

class Human:
    def __init__(self,age,name):
        self.age =age
        self.name =name
class Dancer:
    def __init__(self,style):
        self.style =style
class Student(Human,Dancer):
    def __init__(self,age,name,style):
        Human.__init__(self,age,name)
        Dancer.__init__(self,style)

obj1 =Student(20,'suresh','Hip')
print(obj1.age)
print(obj1.name)
print(obj1.style)


#polymorphism overriding
class Bank:
    def __init__(self):
        return

#class ICICI(Bank):
  #  def __init__(self):
 #       return 10.5

#voerride = ICICI()
#print(voerride.ICICI)


# overloading-same method/thing will be behaves differently based on paramerters

class Myname:
    def __init__(self,name=None):
        if name is not None:
            print("helllo",name)
        else:
            print('pls enter ur name: ')
b1=Myname('suresh')

#ex 2
class Movie:
    def movies(selfself,name=None):
        if name=='RRR':
            print('Its rajamouli direction')
        if name =='Uppena':
            print('its Chitti direction')
        if name is None:

            print('please enter movie name')
m1 =Movie()
m1.movies('RRR')
m1.movies('Uppena')



# Class method












