def add(a,b):
    print a+b
    return;
a=input("Enter a:")
b=input("Enter b:")
add(a,b)

def str(str1):
    print "str1 :",str1
    return;
str("Hello!Have a great day")

def lists(list1):
    list1.append([1,3,5,7,9])
    print "inside listsfunc : ",list1
    return;
list1=[2,4,6,8]
lists(list1)
print "outside listsfunc : ",list1

def list(list1):
    list1=[1,3,5,7,9]
    print "inside listsfunc : ",list1
    return;
list1=[2,4,6,8]
list(list1)
print "outside listsfunc : ",list1




