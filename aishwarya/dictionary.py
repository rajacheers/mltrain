1)# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}



2)Accessing

my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))



3)Changes

my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)


4)Deleting the value

squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  



# remove all items
squares.clear()


5)Iterating


squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])


#Output

1
9
81
25
49



6)squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares))
