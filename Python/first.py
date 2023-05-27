"""x=2
y=2

print(x+y)
name = 'pankaj'+ ' solanki'

print(name)
print(name[0])
print(name[8])
print(name[-1])
print(name[0:3])

print("my name is " + name)
print(len(name))"""

"""nums  = [10,12,20,14,50]
print(nums)
print(nums[0])
print(nums[-1])
print(nums[3:])
names = ['pankaj','jhon','kiran']
print(names)
values = ['pankaj',9.5,25]
print(values)
mil = [nums,names,values]
print(mil)

nums.append(45)
print(nums)
nums.insert(2,100)
print(nums)
nums.remove(20)
print(nums)
nums.pop()
print(nums)

del nums[2:]
print(nums)

nums.extend([29,12,14,36])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
print(sorted(nums))

nums = 5
print(id(nums))
name ='pankaj'
print(id(name))
print(type(nums))


tup = (21,36,25,30)
print(tup)
print(tup[1])
#tup[1] = 50
 

s = {22,25,14,21,50}
print(s) 
s = {10,15,20,45,50,10}
print(s)
#print(s[1])
s.add(500)
print(s)
"""

"""x = int(input("enter fisrt number: "))
y = int(input("enter second number: "))
sum = x+y
print(sum)

result = eval(input("enter a char: "))
print(result)


data = {1:'pankaj',2:'vikas',4:'rakhi'}
print(data)
print(data[4])
print(data.get(3,'Not found'))
print(data.get(1,'Not found'))

keys = ['pankaj','rakhi','vikas']
values = ['python','c++','java']

data = dict(zip(keys,values))
print(data)
data['ramika'] = 'html'
print(data)
del(data['vikas'])
print(data)


prog = {'JS':'Atom','css':'vs code','python':['pycharm','sublime'],'java':{'JSE':'netbeans','JEE':'Eclipse'}}
print(prog)
print(prog['JS'])
print(prog['python'][1])
print(prog['java']['JEE'])


print(list(range(0,10)))
print(list(range(2,20,2)))


#operators
#1 Airthmetic
x=2
y=3
print(x+y) # - * / 

#Assignment =
x=x+2
print(x)
x+=2
print(x)
a,b=5,6
print(a)
print(b)


# Unary
n = 7
n = -n
print(n)

#Relational > < =

print(a<b)
print(a==b)

# swap 2 numbers
# using 3rd variable

a = 5
b = 8
a,b=b,a
'''temp = a
a = b
b = temp'''
print(a, b)



#complement
print(~12)
#bit wise 
print(12&13)



#math functions
import math
x = math.sqrt(25)
print(x)
print(math.ceil(4.8))
print(math.floor(4.8))
print(math.pow(2,3))
print(math.pi)
print(math.e)
# other way to use (Alies)
import math as m
y = m.sqrt(625)
print(y)


# else elif if
x = 3
r = x % 2
if r == 0:
    print("Even")
    if x>5:    #nested if 
        print("greater")
    else:
        print("not greater")    
else:
    print("odd")


x = 5
if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("threee")
elif x == 4:
    print("four")
else:
    print("not found")


##loops
i = 1
j = 1
while i <= 1:
    print("pankaj is good boy", end="")
    while j <= 4:
        print("pankaj roks", end="")
        j += 1
    i += 1
    print()


# for loops 
for i in range(1,21):
    if(i%5!=0):
        print(i)
    
    """

# Break continue pass

"""available = 10
x = int(input("how many condies you want: "))

i = 1
while i<=x:
    if i >available:
        print("we have only these condies ")
        break
    print("Candy")
    i+=1
print("thaks for using")   


#continue
for i in range (1,101):
    if i%3==0 or i%5==0 or i%6==0:
        continue
    print(i)


# pass

for i in range(0, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)




# patterns 

for i in range(4):
    for j in range(4):
        print('#',end=' ')
    print() 



for i in range(4):
    for j in range(i+1):

        print('#',end=' ')
    print()     


for i in range(4):
    for j in range(4-i):
      print('#',end=' ')
    print()     



# for else

nums = [17, 16, 18, 21, 22]
for i in nums:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Number not present")


#prime or not
x = int(input("enter a number: "))
for i in range (2,x):
    if(x%i==0):
        print('not prime')
        break
else:
    print("prime")        


#Arrays
import array as arr
vals = arr.array('i',[5,9,8,4,2])
char = arr.array('u',['p','a','n','k','a','j'])
print(vals.buffer_info())
print(vals.append(45))

print(vals[0])
vals.reverse()
print(vals)
for i in range(len(vals)):
    print(vals[i])
for i in vals:
    print(i)
for i in char:
    print(i)

#creteating a new array
newArr = arr.array(vals.typecode, (a*a for a in vals))   
for i in newArr:
    print(i) 
    


# inpuut from user in array 
from array import *
arr = array('i',[])
n = int(input("enter the lenght of the array: "))
for i in range(n):
    x = int(input("enter the number : "))
    arr.append(x)
print(arr)  
#manually serach index 
val = int(input("enter the value to serach: "))
k =0
for i in arr:
    if(i==val):
        print(k)
        break
    k+=1 
#by function
print(arr.index(val))   


# numpy i python
from numpy import *

# different ways if creating an array in numpy
# 1.array()
arr = array([1, 3, 4, 5, 6, 7, 8],float)  # no need to specify data type of array
print(arr.dtype)
print(arr)


# 2.linspace()
arr = linspace(0,15,5)
print(arr)

# 3. arange()
arr = arange(1,15,2)
print(arr)

# 4. logspace()
arr = logspace(1,40,3)
print(arr)

# 5. zeros()
arr = zeros(5)
print(arr)


# 6.ones()
arr = ones(5,int)
print(arr)



#copying an array
from numpy import *
arr1 = array([1,6,8,5,9])
arr2 = arr1.view() # shallow copy 
arr2 = arr1.copy() # deep copy 
arr1[1] = 100
print(arr2)
print(sort(arr1))
print(concatenate([arr1,arr2]))
"""

# matrix in pyhton(multidimentional array)

# from numpy import *

"""
arr1 = array([
    [1,2,3,10],
    [4,5,6,7]
])
print(arr1.dtype) # guve data type
print(arr1.ndim)  # give number of dimesions
print(arr1.shape) #give number of rows and col
print(arr1.size)  # give the size of array

arr2 = arr1.flatten() #2d to 1d array
print(arr2)

arr3 = arr2.reshape(2,2,3) # 1d to 2d and 3d array
print(arr3)

mat = matrix(arr1) # converting an array to matrix
mat1  = matrix('1 2 3;6 4 5;1 6 7')
mat2 =   matrix('1 2 3;6 4 5;1 6 7')
print(diagonal(mat1))
print(mat1.min())
print(mat1.max())

mat3 = mat1 + mat2
print(mat3)
mat3 = mat1 * mat2
print(mat3)



# Functions in python
def greet():
    print("my name is pankaj solanki")
    print("good morning")


def add_sub(x,y):
    c = x+y
    d = x-y
         
    
    #print(c) # printing 
    return c,d # returning result
greet()     
result1, result2  = add_sub(5,4) 
print(result1,result2)



# arguments in python
def person(name, age=18):
    print(name)
    print(age)


person("Pankaj", 20)


# variable length arg
def sum(a, *b):
    c = a
    for i in b:
        c = c + i

    print(c)


sum(5, 2, 6, 34)



# keyworded variable lentgh arg
def person(name, **data):
    print(name)
    
    for i,j in data.items():
        print(i,j)

person("pankaj", age=20, city="Agra", mob=9997692641)  # variable lentgh arg

# passing a list to a function
def count(lst):
    for i in lst:
        if len(i)<5:
            print(i)


lst = ["pankaj", "tushar", "vikas", "ravi", "ram"]

count(lst)



# fibonacci sequence
def fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:    
      print(a)
      print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


n = int(input("enter a number: "))
if n > 0:
    fib(n)
else:
    print("enter an positive number!")    



# factorial of a number
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


n = int(input("enter a number: "))
if n >= 0:
    result = fact(n)
    print(result)
else:
    print("enter an positive number!")



# Recursion in python (factorial)
def fact(n):
    if n ==0:
        return 1
    return n * fact(n - 1)


n = int(input("enter a number: "))
result = fact(n)
print(result)


#filter(), map() and reduce()

from functools import reduce
#def is_even(n):
 #   return n%2==0

nums = [2,4,6,8,9,4,12]
evens = list(filter(lambda n : n%2==0,nums))#using lambda function

#map()
doubles =  list(map(lambda n : n*2,evens))

#Reduce()
sum = reduce(lambda a,b : a+b,doubles)


print(evens)
print(doubles)
print(sum)



#Modules in python
from calc import *
a = 9
b = 7
c=add(a,b)
print(c)
d=sub(a,b)
print(d)
e=multi(a,b)
print(e) 
f=div(a,b)
print(f)


#OOPS in Python
#class & objects
class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Config is: ", self.cpu,self.ram)
   
    
comp1 = computer('i5',16)
comp2 = computer('Ryzen 5',8)
computer.config(comp1)
comp2.config()
"""
class person:
    def __init__(self):
        self.name = "pankaj"
        self.age = 20
       
 
p1 = person()
p2 = person()
p1.name = "Rakhi"
p1.age = 16   
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)    


