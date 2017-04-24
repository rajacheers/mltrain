print "Size of the list:"
n=int(input())
user=raw_input("Enter list1 of numbers : ")
a=[int(n) for n in user.split(' ')]
print "Enter list2 of strings : "
b=[]
for x in range(5):
    x=input("")
    b.append(x)
print "Enter list3 of numbers and strings : "
c=[]
for x in range(5):
    x=input("")
    try:
        c.append(int(x))
    except ValueError:
        c.append(x)
print "The entered lists are"
print(a[:])
print(b[:])
print(c[:])
print "list[0]:",a[0]
print "list[1:3]:",b[1:3]
print "list[:2]:",c[:2]
a[2]=1000;
print "updatedlist:",a
del b[1];
print "remove",a.remove(1)
print "afterdeletingelement:",b[1]
print "len1:",len(a)
print "len2:",len(b)
print "len3:",len(c)
print "concat:",a+[0,0,0]
print "repeat:",['Hello']*3
a.reverse()
print "reverse:",a
c.sort()
print "sort:",c
b.insert(2,"XXXXX")
print "insert:",b




