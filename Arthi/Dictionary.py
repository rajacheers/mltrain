import operator

#program-1

a = {1:3,8:4,2:4,5:10}
sorted_a = sorted(a.items(),key=operator.itemgetter(0))
print("in decending : ",sorted_a )
sorted_b = sorted(a.items(),key=operator.itemgetter(0),reverse = True)
print("in acending : ",sorted_b )

#program-2

dict_exam = {'animal':'dog','vegetable':'Tomato'}
key = input("enter the key to check : ")
result = key in dict_exam
if result is True:
	print("given key is available")
else:
	print("given key is not available")
