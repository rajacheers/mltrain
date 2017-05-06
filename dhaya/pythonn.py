# This program prints Hello, world!
print('Hello, world!')

# This program adds two numbers
num1 = 1
num2 = 6
sum = num1 + num2
print('The total is :',sum)

# This program adds two numbers with run time input
num1 = input('Enter number 1 :' )
num2 = input('Enter number 1 :')
sum = float(num1) + float( num2)
sum = float(num1) - float( num2)
sum = float(num1) * float( num2)
sum = float(num1) / float( num2)
print('The total is :',sum)

# Python Program to calculate the square root
num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print(num_sqrt)

#Looping programs
num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")

#factorial number
num = 10
factorial = 1
if num > 0:
  for i in range(1,num+1):
    factorial=factorial*i
  print(factorial)
elif num<0:
    print("sorry")
else:
    print("again sorry")

#Function with values
def bitcoin_to_usd(bitcoin):
    usd = bitcoin * 527
    return usd

print(bitcoin_to_usd(1))
x=bitcoin_to_usd(2)
print(x)




