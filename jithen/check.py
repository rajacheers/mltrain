
import func
import random

age = 27

if age > 21:
   print("hello")

name = "helo"

if name is "helo":
 print("name is  hello")
 print("name is  hello")
elif name is "hello":
 print("name is helo")
else:
   print("xxxx")


x =[1,2,3]
print(x)

#for loop

food =["rice", "briyani", "sambar"]
i=0;
for indx in food[:2]:
    print(indx)
    print(len(indx))
    print(i)
    i = i + 1

#range

for x in range(10):
    print(x)
    print("x")

# range(start,end,incrmeent)
for x in range(1,10,2):
    print(x)
    print("x")

#whiile

tamil = 8
while (tamil < 10):
      print("tamil")
      tamil += 1;

#comments and break:


print("tamil" + "arasu")
print("tamil",10)

print(10 + 20)

#break

magicNumber = 26
for n in range(10):
    if n == 26:
       print(n,"is the magic")
       break
    else:
       print(n)


for n in range(101):
    if (n%4 ==0):
       print(n)
 



#continue
numbers = [1,2,7,8,9,4,7]

print("numbers avaibale") 

for i in range(11,20):
    if i in numbers:
       continue
    else:
        print(i)

#functions:

# to create function:
# 1. #def function_name():
# 2. any lines after that.. should be indenated


def hello():
   print("hello")
   print(1+2)

#to call the function:
hello()
hello()
hello()


#function examples:

def bitcoin_to_usd(bitcoin):
    usd = bitcoin * 527
    print(usd)

bitcoin_to_usd(1)
bitcoin_to_usd(100.24)
bitcoin_to_usd(100)


#function with return values

def bitcoin_to_usd(bitcoin):
    usd = bitcoin * 527
    return usd

print(bitcoin_to_usd(1))
x=bitcoin_to_usd(2)
print(x)


#function with default values

def bitcoin_to_usd(bitcoin=2):
    usd = bitcoin * 527
    return usd

print(bitcoin_to_usd())
x=bitcoin_to_usd(2)
print(x)


def get_gender(sex = "unknown"):
    if sex is 'a':
       print("sex is male")
    elif sex is 'b':
       print("sex is female")
    else:
       print(sex)


get_gender('a')
get_gender('b');
get_gender();
get_gender('z');


#variable scope
a=3
def fun1():
    a = 1234
    print(a)

def fun2():
    print(a)


fun1()
fun2()


#keyword arguments:
def func1(s = 'tamil', v= 'ate', o = 'apple'):
    print(s,v,o)


func1() 
func1("s","v","o")
func1(o="mang")


#flexible_numbers of arguments

def add_numbers(*val):
    total = 0
    for a in val:
        total += a
    print total   


add_numbers(1,2,3,4)

#unpacking arguments:
def add_numbers(*val):
    total = 0
    for a in val:
        total += a
    print total   


num = [1,2,3,4]
add_numbers(*num)


#sets:
groceries = {'grains', 'moong', 'dal' ,'rice' ,'grains'}
print (groceries)

if 'grains' in groceries:
    print('grain is there')


#dictionaries: - key value pairs

classmates ={'tony':'x1', 'tamil':'x2','jim':'x3'}
print(classmates)
print(classmates['tony'])

for k,v in classmates.items():
    print(k + v)


#modules:


func.bitcoin_to_usd(1)
func.bitcoin_to_usd(100.24)
func.bitcoin_to_usd(100)

print(random.randrange(1,90))






















    



    
    









      




