1)def greet(name):
	print("Hello, " + name + ". Good morning!")

#input:  greet('Paul')
#output: Hello, Paul. Good morning!


2)Function with return value

def absolute_value(num):
	if num >= 0:
		return num
	else:
		return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))


3) Scope of a variable 


def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

#Output

Value inside function: 10
Value outside function: 20


4) Tuple in function


def greet(*names):

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")


#Output
Hello Monica
Hello Luke
Hello Steve



4)Lamda function with filter()

# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)
Hello John
