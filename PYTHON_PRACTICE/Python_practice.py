#python : high level, interpreted, objrct oriented programming language known for its simple and readable syntax.
# Used in:Web Development, Data Science, Machine Learning, AI,Automation,Cybersecurity,Game Development 
#1.variables: is a named container used to store data.
from tracemalloc import start, stop


name = "John"
age = 20
height = 5.8
#Rules:
#Cannot start with a number
#Case-sensitive
#No spaces
#Use _ instead of spaces
#2.constants: are variables whose values cannot be changed once assigned.
PI = 3.14159
GRAVITY = 9.8
#3.Data types: is a classification of data which tells the compiler or interpreter how the programmer intends to use the data.
#Common data types in python:
#int: whole numbers
#float: decimal numbers
#str: sequence of characters
name = "Alice"
city = 'New York'

print(name)
print(city)

#String Operations:
#len(): returns the length of a string
#upper(): converts a string to uppercase
#lower(): converts a string to lowercase
#strip(): removes whitespace from the beginning and end of a string
#replace(): replaces a substring with another substring
#split(): splits a string into a list of substrings
#join(): joins a list of strings into a single string

#bool:represents only two values. True or False
#4.Operators: are symbols that perform operations on variables and values.
#Arithmetic operators: +, -, *, /, %, **, //
#Comparison operators:return Boolean values. ==, !=, >, <, >=, <=
#Logical operators:combine Boolean expressions. and, or, not
#5.Statements: are instructions executed by Python
# Conditional statements: are used to perform different actions based on different conditions.
#if age >= 18:
#   print("You are an adult.")
#elif age < 18 and age >= 13:
#   print("You are a teenager.")
#else:
#   print("You are a child.")

#6.Loops: are used to execute a block of code repeatedly.
#for i in range(5):
#   print(i)
#while age < 30:
#   print(age)
#7.Functions: are blocks of code that perform a specific task and can be reused.
def print_info():
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")


name = "Sri"
age = 25
height = 170

def print_info():
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
print_info()

#8.Lists: are used to store multiple items in a single variable.
fruits = ["apple", "banana", "orange"]
print(fruits)
#9.Tuples: are used to store multiple items in a single variable. Tuples are immutable.
colors = ("red", "green", "blue")
print(colors)
#10.Dictionaries: are used to store data in key-value pairs.
person = {"name": "John", "age": 30, "city": "New York"}
print(person)
#11.Sets: are used to store multiple items in a single variable. Sets are unordered and unindexed.
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
#12.File handling: is used to read and write files in python.
#with open("example.txt", "w") as file:
#   file.write("Hello, World!")
#with open("example.txt", "r") as file:

#type casting: is used to convert one data type to another.
#implicit type casting: is done automatically by python by converting a smaller data type to a larger data type.
a = 10
b = 5.5

result = a + b

print(result)
print(type(result))

#explicit type casting: is done manually by the programmer.
c = 10
d = float(c)
print(d)
print(type(d))
#dynamic typing: is a feature of python where the type of a variable is determined at runtime.
x = 10
print(type(x))

x = "Python"
print(type(x))

x = 5.5
print(type(x))

############################class 2 #######################
#PYTHON DATA COLLECTIONS
#Python has 5 main collection data types:
#STRING: is a sequence of characters.
#Strings are enclosed in single (' ') or double (" ") quotes.
#Strings are immutable (cannot be changed).
name = "Alice"

print(name)
print(name[0])      # First character
print(len(name))    # Length of string
print(name.upper())
#2.LIST: is a collection of items which is ordered and changeable. Allows duplicate members.
numbers = [10, 20, 30, 40]

print(numbers)
numbers.append(50)
print(numbers)
#Program to calculate the sum of all numbers stored in a list
numbers = [10, 20, 30, 40]

sum = 0

for num in numbers:
    sum += num

print("Sum =", sum)
#USING INDEXES TO ACCESS ELEMENTS IN A LIST.
numbers = [10, 20, 30, 40]

sum = 0

for i in range(len(numbers)):
    sum += numbers[i]

print(sum)
#3.TUPLE: is a collection of items which is ordered and unchangeable. Allows duplicate members.
marks = (80, 90, 75)

print(marks)
print(marks[1])

#4.SET: is a collection of items which is unordered and unindexed. No duplicate members.
fruits = {"Apple", "Banana", "Apple"}

print(fruits)
#5.DICTIONARY: is a collection of items which is unordered, changeable and indexed. No duplicate members.
student = {
    "name": "John",
    "age": 20,
    "marks": 90
}

print(student["name"])
print(student["marks"])

#RANGE FUNCTION: is used to generate a sequence of numbers.
#SYNTAX 
# range(stop)
#range(start, stop)
#range(start, stop, step)

for i in range(5):
    print(i)
#EXAMPLE 2
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])
#INDEX: is the position of an element in a list, tuple or string. Indexes start from 0.
colors = ["Red","Blue","Green"]

print(colors[0])
print(colors[1])
print(colors[2])

#for loop: is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#Program: Add Natural Numbers Find 1 + 2 + 3 + ... + n
n = 10

sum = 0

for i in range(1, n+1):
    sum += i

print("Sum =", sum)
#Example : Print Each Character in a String.
name = "Python"

for ch in name:
    print(ch)
#while loop: is used to execute a block of code as long as a condition is true.
i = 1

while i <= 5:
    print(i)
    i += 1

#ADD NATURAL NUMBERS USING WHILE LOOP.
n = 10

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(sum)

#REVERSE A LIST:
#numbers = [10,20,30,40,50]

numbers.reverse()

print(numbers)
#Reverse Using a while Loop.
#numbers = [10, 20, 30, 40, 50]

i = len(numbers) - 1

while i >= 0:
    print(numbers[i])
    i -= 1
#COUNT: is used to count the number of occurrences of an element in a list, tuple or string.
# eg : COUNT VOWELS IN A LIST 
word = input("Enter a word: ")

print("Number of a =", word.count("a"))
print("Number of e =", word.count("e"))
print("Number of i =", word.count("i"))
print("Number of o =", word.count("o"))
print("Number of u =", word.count("u"))
#Count User Input in a List.
#numbers = [1, 2, 3, 2, 4, 2, 5]

num = int(input("Enter number to count: "))

print("Count =", numbers.count(num))

#CHECK : is used to check if an element exists in a list, tuple or string.
#word = input("Enter a word: ")
if "a" in word:
    print("a is present in the word.")
if "e" in word:
    print("e is present in the word.")
if "i" in word:
    print("i is present in the word.")
if "o" in word:
    print("o is present in the word.")
if "u" in word:
    print("u is present in the word.")

#palindrome : is a word, phrase, number, or other sequence of characters which reads the same backward as forward.
#word = input("Enter a word: ")

#if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Break statement: is used to exit a loop when a certain condition is met.
for i in range(1,10):

    if i == 6:
        break

    print(i)

#Continue statement : is used to skip the current iteration of a loop and move to the next iteration.
for i in range(1,10):

    if i == 5:
        continue

    print(i)

#len: is used to get the length of a list, tuple or string.
numbers = [10, 20, 30, 40, 50]

sum = 0

for i in range(len(numbers)):
    sum += numbers[i]

print("Last Index =", i)
print("Sum =", sum)


