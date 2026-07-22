#containers:  lists, tuples, sets, dictionaries, strings.
#string slicing:  string[start:end:step]
text = "Python Programming"

print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[::2])
print(text[::-1])
#string properties : Ordered,immutable,
#concatenate strings using + operator
first = "Hello"
second = "World"

result = first + " " + second

print(result)
#using join 
words = ["Python","Java","C++"]

print("-".join(words))
#basic built in string methods
print(text.upper())
print(text.lower())
print(text.capitalize())
#print(text.replace())
print(text.split())
#print formatting
#using comma
name="John"
age=20

print(name,age)
#using format
name="John"
age=20

print("My name is {} and age is {}".format(name,age))
#using f string
name="John"
age=20
print(f"My name is {name} and age is {age}")
#built in regular expressions :  Regular expressions are used for pattern searching.
import re
text="My phone number is 12345"
result=re.search("12345",text)
print(result)

text="apple,orange,banana"
print(re.split(",",text))

#list slicing
nums=[10,20,30,40,50]

print(nums[1:4])
print(nums[::-1])

#make list double: using multiplication operator
numbers=[1,2,3]
double=numbers*2
print(double)
#Basic List Methods
#apppend: adds an element to the end of the list
a=[1,2]
a.append(3)
print(a)
#insert: adds an element at a specific index
a=[1,3]
a.insert(1,2)
print(a)
#remove: removes the first occurrence of a specific element
a=[1,2,3]
a.remove(2)
print(a)
#pop: removes and returns the last element of the list
a=[10,20,30]
x=a.pop()
print(x)
print(a)
#nested lists: A list can contain other lists as elements, creating a nested structure.
data=[
    [1,2],
    [3,4]
]

print(data[0])
print(data[1][0])

#Matrix : A matrix is a two-dimensional list, where each element is a list itself.
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0])
print(matrix[1][1])

#three lists in a matrix
matrix=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

for row in matrix:
    print(row)
#list comprehension: List comprehension is a concise way to create lists using a single line of code.
#normal method
numbers=[]
for i in range(5):
    numbers.append(i)

print(numbers)
#list comprehension method
numbers=[i for i in range(5)]
print(numbers)
#with condition 
even=[x for x in range(10) if x%2==0]
print(even)
#ADVANCED LIST OPERATIONS
#SORTING
nums=[5,2,8,1]
nums.sort()
print(nums)
#REVERSE:
nums.reverse()
print(nums)
#EXTEND
a=[1,2]
b=[3,4]

a.extend(b)

print(a)
#COPY
a=[1,2,3]

b=a.copy()

print(b)

#TUPLES :Tuples are ordered, immutable collections of elements. They are defined using parentheses ().:
t=(10,20,30)
print(t)

print(t[0]) #tuple indexing
print(t[1:3]) #tuple slicing
#sets: Sets are unordered collections of unique elements. 
# They are defined using curly braces {} or the set() constructor.
s={1,2,3,3}

print(s)
#set discard: removes an element from the set if it exists; does nothing if the element is not present.
s={1,2,3}

s.discard(2)

print(s)
#set clear : removes all elements from the set.
s={1,2,3}

s.clear()

print(s)
#DICTIONARIES: Dictionaries are unordered collections of key-value pairs.
student={
    "name":"John",
    "age":20
}
print(student)
#CONSTRUCTING DICTIONARIES: Dictionaries can be constructed using curly braces {} or the dict() constructor.
#USING{}
person={
"name":"Alex",
"age":25
}
print(person)
#USING DICT()
person=dict(name="Alex",age=25)
print(person)

#DICTIONARY METHODS: Dictionaries have various methods for manipulating key-value pairs.
#NESTED DICTIONARIES: Dictionaries can contain other dictionaries as values, creating a nested structure.
students={
    "student1":{
        "name":"John",
        "age":20
    },
    "student2":{
        "name":"Sam",
        "age":22
    }
}

print(students["student1"]["name"])

#dictionary comprehension: Dictionary comprehension is a concise way to create dictionaries using a single line of code.
numbers={x:x*x for x in range(5)}

print(numbers)

#copying dictionaries: You can create a copy of a dictionary using the copy() method or the dict() constructor.
#shallow copy: creates a new dictionary that references the same objects as the original dictionary.
import copy

a=[[1,2],[3,4]]

b=copy.copy(a)

b[0][0]=100

print(a)
print(b)

#deep copy(): creates a new dictionary that recursively copies all objects from the original dictionary, ensuring that changes to the copy do not affect the original.
import copy
a=[[1,2],[3,4]]
b=copy.deepcopy(a)
b[0][0]=100
print(a)
print(b)
