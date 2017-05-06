str1=input("Enter your string1 : ")
str2=input("Enter your string2 : ")
print(str1)
print(str2)
print "My first string is %s and the second string is %s"%(str1,str2)
print "str*3:",(str1*3)
print "concat:",(str1+str2)
len1 = len(str1)
print "length1:",len1
len2 = len(str2)
print "length2:",len2
print "fetchrange:",str1[1:len1-2]
print "fetchchar:",str2[3]
print "update:",str2[:len2-3]+'XXXXX'
print "capital:",str1.capitalize()
print "digit:",str1.isdigit()
print "lower:",str2.lower()
print "upper:",str1.upper()
print "maxrepeat:",max(str1)
print "minrepeat:",min(str2)
print "replace:",str1.replace("is","was")
print "split:",str2.split('.')

















