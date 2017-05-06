1)# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed datatypes
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]



2)Accessing element in list


my_list = ['p','r','o','b','e']

# Output: p
print(my_list[0])


# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])    

# Output: 5
print(n_list[1][3])

#Negative indexing

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])


3)Slicing the list


my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])


4) Append and Extend 


odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)


5) delete

# delete one item
del my_list[2]

# delete multiple items
del my_list[1:5]  


# delete entire list
del my_list  

5) sort

my_list = [3, 8, 1, 6, 0, 8, 4]
my_list.sort()
# Output: [0, 1, 3, 4, 6, 8, 8]
print my_list

my_list.reverse()
# Output: [8, 8, 6, 4, 3, 1, 0]


6)pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)


7) For loop using list


for fruit in ['apple','banana','mango']:
    print("I like",fruit)

#Output

I like apple
I like banana
I like mango


Tuple

1)# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

2)my_tuple = ['p','e','r','m','i','t']

# Output: 'p'
print(my_tuple[0])


# Output: 't'
print(my_tuple[-1])


my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])
print(my_list)


# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))


# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)



