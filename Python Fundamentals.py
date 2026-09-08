# Python fundamentals
#Python Variables and Literals

# assign value to book_title variable
book_title = 'Python Programming'

print(book_title)
print ()


#Changing the Value of a Variable in Python
book_title = 'Introduction to Python'
print(book_title)

# assigning a new value to message
message = 'Welcome to Python Programming'

print(message)
print ()

#Assigning multiple values to multiple variables 
a, b, c = 5, 3.2, 'Hello all'

print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello all
print ()

subject1 = subject2  = 'Computer Science'

print (subject1)  # prints Computer Science
print (subject2)  # prints Computer Science
print ()




#Python Type Conversion
#Converting integer to float
integer_number = 567
float_number = 5.67

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))
print ()


#Addition of string and integer Using Explicit Conversion
num_string = '14'
num_integer = 27

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
print ()



#Python Basic Input and Output
#Python Output
print('Exploring the digital universe!')
print ()

#Python Print Statement
print('Mission started succesfully.')
print('The system is ready')
print('Welcome, space explorer!')
print ()


#Python print() with end Parameter
print('Launching', end= ' ')

print('the next adventure!')
print() 


#Python print() with sep Parameter
print('Moon', 2027, 'Artemis III', sep= '. ')
print ()



#Print Python Variables and Literals
mission_year = 2027

destination = "The Moon"

# print literals     
print(384400)

# print variables
print(mission_year)
print(destination)
print ()

print('Artemis III ' + 'will return ' + 'to the Moon.') 
print('The mission ' + 'is planned for ' + '2027.')
print('Astronauts ' + 'will explore ' + 'the Moon.')
print()



#Print Concatenated Strings
print('The rocket ' + 'is ready ' + 'for launch.')
print('The crew ' + 'travels ' + 'toward the Moon.')
print('A new mission ' + 'begins ' + 'in 2027.')
print()

#Output formatting
x = 10
y = 15

print('The value of x is {} and y is {}'.format(x,y))
print('The value of x is {1} and y is {0}'.format(x,y))
print('The value of x is {x} and y is {y}'.format(x=x,y=y))
print()


#Python User Input
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))
print()



#Python Operators
#Python Arithmetic Operators
x = 14
y = 6
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)
print('x ** y = ',x**y)
print('x % y = ',x%y)
print()


#Comparison operators
x = 20
y = 14
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)
print()


#Logical operators
x = True
y = False
print('x and y is',x and y) 
print('x or y is',x or y)
print('not x is',not x)
print('not y is',not y)
print() 


#Bitwise operators
x = 10
y = 4
print('x & y =',x & y)
print('x | y =',x | y)
print('x ^ y =',x ^ y)
print('~x =',~x)
print('x << 2 =',x << 2)
print('x >> 2 =',x >> 2)
print ()


#Assignment operators
x = 5
print('x =',x)
x += 3
print('x += 3 is',x)
x -= 3
print('x -= 3 is',x)
x *= 3
print('x *= 3 is',x)
x /= 3
print('x /= 3 is',x)
print('x //= 3 is',x)
x **= 3
print('x **= 3 is',x)
print('x %= 3 is',x)
print()


#Special operators
#Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
print(x3 is not y3)
print()

#Membership operators
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)
print('b' not in y)
print()





