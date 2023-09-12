# -*- coding: utf-8 -*-
"""Python Day.1 PS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wnUrEnlOJDpsdouTkOuQ57wmTgVBVAGL

1. Manipulate using a list.
  a)To add new elements to the end of the list
  b)To reverse elements in the list.
  c)To display the same list of elements multiple times
  d)To concatenate two list
  e)To sort the elements in the list in ascending order
"""

#a) To add new elements to the end of the list
ls=[41,53,82,11,4,9,3]
ls.append(24)
print(ls)

#b)To reverse elements in the list.
ls=[41, 53, 82, 11, 4, 9, 3, 24]
ls.reverse()
print("The reverse order of the list is",ls)

#c)To display the same list of elements multiple times
ls="Priya "
new_ls = 5*ls
print(new_ls)

#d)To concatenate two list
ls=[41, 53, 82, 11, 4, 9, 3, 24]
ls_1=["hello","priya"]
ls_2 = ls+ls_1
print("Concatination of two lists are ",str(ls_2))

#e)To sort the elements in the list in ascending order
ls=[41, 53, 82, 11, 4, 9, 3, 24]
ls.sort()
print("Sorted list is",ls )

"""2.Write a python program to do in the tuples.
  a).Manipulate using tuples.
  b).To add ne elements to the end of the tuples.
  c).To reverse elements in the list
  d).To display the elements of the same tuple multiple times.
  e).To concatenate two tuples.
  f).To sort the elements in the list in ascending order
"""

#a).Manipulate using tuples.
# we can not change the values of the tuple becaude tuples are immutable or unchanged.So once a tuple is created ,we can not change its value

#b).To add new elements to the end of the tuples.
tp = (6,3,5)
tp_append = tp + (8,7)
print(tp_append)
print(tp)

#c).To reverse elements in the tuple
tp = (28,99,56,43)
tp = tp[::-1]
print("The reversed tuple is:",tp)

#d).To display the elements of the same tuple multiple times.
tp=('priya ')
new_tp = 5 * tp
print(new_tp)

#e).To concatenate two tuples.
tp = (2,5,8,1)
tp_1 = (71,55,94)
res = tp + tp_1
print("The concatenation of the tuple is "+str(res))

#f).To sort the elements in the list in ascending order
tp=(67,34,96,13,6,24)
res = tuple(sorted(tp))
print("Sorted tuple is",res)

"""3. Write a python program  to implement the following using list
  a).Create a list with integers(minimum 10 characters)
  b).How to display the last number in the list.
  c).Command for displaying the values from the list[0:4]
  d).Command for displaying the values from the list[2:]
  e).Command for displaying the values from the list[:6]

"""

#a).Create a list with integers(minimum 10 characters)
ls = [64,24,75,98,56,29,97,36,37,48,17,20]
print(ls)

#b).How to display the last number in the list.
ls = [64,24,75,98,56,29,97,36,37,48,17,20]
print(ls[-1])

#c).Command for displaying the values from the list[0:4]
ls = [64,24,75,98,56,29,97,36,37,48,17,20]
print(ls[0:4])

#d).Command for displaying the values from the list[2:]
ls = [64,24,75,98,56,29,97,36,37,48,17,20]
print(ls[2:])

#e).Command for displaying the values from the list[:6]
ls = [64,24,75,98,56,29,97,36,37,48,17,20]
print(ls[:6])

"""4.Write a python program :tuple1=(10,50,20,40,30)
  a).To display the elements 10 to 50 from tuple1
  b).To dispaly the length of the tuple1
  c).To find the minimum element from tuple1
  d).To add the elements in the tuple1
  e).To display the same tuple1 multiple times
"""

tuple1=(10,50,20,40,30)
print(tuple1)

#a).To display the elements 10 and 50 from tuple1
tuple1=(10,50,20,40,30)
print(tuple1[0],tuple1[1])

#b).To dispaly the length of the tuple1
tuple1=(10,50,20,40,30)
print(len(tuple1))

#c).To find the minimum element from tuple1
tuple1=(10,50,20,40,30)
print(min(tuple1))

#d).To add the elements in the tuple1
tuple1=(10,50,20,40,30)
print(sum(tuple1))

#e).To display the same tuple1 multiple times
tuple1=(10,50,20,40,30)
print(3*(tuple1))

"""Write a python program:
  a).to calculate the length of a string
  b).to reverse words in a string
  c).to display the same string multiple times
  d).To concatenate two strings
  e).Str = "South India", using string slicing to display "India"
"""

#a).to calculate the length of a string
s = "Priyanka"
print(len(s))

#b).to reverse words in a string
s = "Priyanka"
print(s[::-1])

#c).to display the same string multiple times
s = "Priyanka "
print(3*s)

#d).To concatenate two strings
s1 = "priyanka "
s2 = "Gunda"
print(s1+s2)

#e).Str = "South India", using string slicing to display "India"
str = "South India"
print(str[6:])

"""6.Perform the following
  a).creating the dictionary.
  b).Accessing values and keys in the dictionary
  c).Updating the dictionary using a function
  d).Clear and delete the dictionary values
"""

#a).creating the dictionary.
d = {'name':'Priya', 'age':22, 'city': 'Guntur'}
print(d)

#b).Accessing values and keys in the dictionary
d = {'name':'Priya', 'age':22, 'city': 'Guntur'}
print("Name:",d['name'])

#c).Updating the dictionary using a function
d = {'name':'Priya', 'age':22, 'city': 'Guntur'}
d['age'] = 21
print('updated dictionary' , d)

#d).Clear and delete the dictionary values
d = {'name':'Priya', 'age':22, 'city': 'Guntur'}
d.clear()
print(d)

d = {'name':'Priya', 'age':22, 'city': 'Guntur'}
del d

"""7.Python program to insert a number to any position in a list"""

ls = [5,2,6,3,7,9]
num = 10
position = 4
ls.insert(position,num)
print("updated list:",ls)

"""8.Python program to delete an element from a list by index"""

ls = [5,2,6,3,7,9]
index = 2
del ls[index]
print("updated list is ",ls)

"""9.Write a program to dispaly a number from 1 to 100"""

for number in range(1,101):
  print(number)

"""10.Write a python program to find the sum of the all items in a tuple"""

tp = (4,7,1,8,9,4,7)
print(sum(tp))

"""12. A list of words is given. Find the words from the list that have their second character in uppercase.
ls=["hello",'Dear','hOw','ARe','You']
"""

ls=["hello",'Dear','hOw','ARe','You']
res = [word for word in ls if word[1].isupper()]
print(res)

"""**Control Structures**

1. Write a python program to find the first N Prime numbers
"""

N = int(input("Enter the value of N: "))
count = 0
num = 2

while count < N:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

"""2.Write the python code that calculates the salary of an employee.Prompt the user to enter the Basic Salary,HRA,TA, and Da. Add these components to calculate the Gross Salary.Also,deduct10% of salary from the gross salary to be paid as tax and display gross minus tax as net salary."""

basic_salary = float(input("Enter the Basic Salary: "))
hra = float(input("Enter the HRA: "))
ta = float(input("Enter the TA: "))
da = float(input("Enter the DA: "))
gross_salary = basic_salary + hra + ta + da
tax = 0.10 * gross_salary
net_salary = gross_salary - tax
print(f"Gross Salary: {gross_salary:.2f}")
print(f"Tax Deduction (10%): {tax:.2f}")
print(f"Net Salary: {net_salary:.2f}")

"""3. Write a python program to search for a string in the given list."""

string_list = ["apple", "banana", "cherry", "date", "fig", "grape"]

search_string = input("Enter a string to search for: ")

found = False

for item in string_list:
    if search_string.lower() == item.lower():
        found = True
        break


if found:
    print(f"'{search_string}' was found in the list.")
else:
    print(f"'{search_string}' was not found in the list.")

"""5.Write a program to display the sum of odd numbers and even numbers that fall between 12 and 37"""

sum_even = 0
sum_odd = 0
a=int(input())
b=int(input())
for num in range(a,b):
    if num % 2 == 0:  # Check if the number is even
        sum_even += num
    else:
        sum_odd += num

# Display the sums
print(f"Sum of even numbers between a and b: {sum_even}")
print(f"Sum of odd numbers between a and b: {sum_odd}")

"""6.Write a python program to print the table of any number"""

number = int(input("Enter a number: "))

print(f"Multiplication table for {number} up to 10:")

for i in range(1, 10+ 1):
    result = number * i
    print(f"{number} x {i} = {result}")

"""7.Write a python program to sum the first 10 prime numbers"""

count = 0
num = 2
prime_sum = 0

while count < 10:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num
        count += 1
    num += 1

print(f"The sum of the first 10 prime numbers is: {prime_sum}")

"""8.Write a python program to implement arithmetic operations using nested if statement"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

"""9.Write a python program to take the temperature in celsius and convert it to fahrenheit"""

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

"""10.Write a python program to find a maximum and minimum number.  """

numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

if not numbers:
    print("The list is empty.")
else:

    max_num = max(numbers)
    min_num = min(numbers)

    print(f"Maximum number: {max_num}")
    print(f"Minimum number: {min_num}")

"""11. Write a program in python to print out the number of seconds in 30-day month 30 days, 24 hours in a day ,60 minutes per day,60 seconds in a minute."""

# Define constants
d= 30
h= 24
m= 60
s= 60

# Calculate the total number of seconds
total= d* h* m *s

# Display the result
print(f"The number of seconds in a 30-day month is: {total}")

"""12.Write a program in python to print out the number of seconds in a year"""

d= 365.25
h= 24
m = 60
s = 60

# Calculate the total number of seconds in a year
t= d * h * m * s

# Display the result
print(f"The number of seconds in a year is approximately: {t:.0f}")

"""13. A high-speed train can travel at an average speed of 150mph, how long will it take a train travelleing at this speed to travel from london to glasgow which which is 414 miles away"""

speed = 150
distance = 414
time_hours = distance / speed
print(f"It will take {time_hours} hours to travel from London to Glasgow at an average speed of 150 mph.")

"""14.write a python program  that defines a variable  called days_in_each_school_year and assign 192 to the variable.The program should then print out the total hour that you spend in school from year 7 to year 11, if each day you spend 6 hours in school days_in_each_school_year = 192"""

days_in_each_school_year = 192
total_school_days = (11 - 7 + 1) * days_in_each_school_year
hours_per_day = 6
total_hours_in_school = total_school_days * hours_per_day
print(f"Total hours spent in school from year 7 to year 11: {total_hours_in_school} hours")

"""15.If the age of Ram, Sam and Khan are input through the keyboard, write a python program to determine the eldest and eldest and youngest of the three"""

ram_age = int(input("Enter the age of Ram: "))
sam_age = int(input("Enter the age of Sam: "))
khan_age = int(input("Enter the age of Khan: "))
if ram_age > sam_age and ram_age > khan_age:
    eldest = "Ram"
elif sam_age > ram_age and sam_age > khan_age:
    eldest = "Sam"
else:
    eldest = "Khan"

if ram_age < sam_age and ram_age < khan_age:
    youngest = "Ram"
elif sam_age < ram_age and sam_age < khan_age:
    youngest = "Sam"
else:
    youngest = "Khan"
print(f"The eldest person is {eldest} with an age of {max(ram_age, sam_age, khan_age)} years.")
print(f"The youngest person is {youngest} with an age of {min(ram_age, sam_age, khan_age)} years.")

"""17.Python program to print the patterns given below:

a).1
   1 1
   1 2 1
   1 3 3 1
   1 4 6 4 1
   1 5 10 10 5 1
   1 6 15 20 15 6 1
"""

n=int(input())
for i in range(n):
  print(''*(n-i),end='')
  print(' '.join(map(str,str(11**i))))

"""b). *
    * *
    * * *
    * * * *
    * * * * *
"""

n=int(input())
myList = []
for i in range(1,n+1):
  myList.append("* "*i)
print("\n".join(myList))

"""c).           *
             *  *
            *  *  *
           *  *  *  *
          *  *  *  *  *
         *  *  *  *  *  *
        *  *  *  *  *  *  *
"""

n = int(input())
k = n-1
for i in range(0,n):
  for j in range(0,k):
    print(end=" ")
  k=k-1
  for j in range(0,i+1):
    print("* ",end="")
  print("\r")

"""d). P
    PY
    PYT
    PYTH
    PYTHO
    PYTHON
"""

str=input("enter the string:")
len=len(str)
for i in range(len):
  for j in range(i+1):
    print(str[j],end="")
  print()