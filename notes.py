#lec 1

from ast import Return


print("hello world ")
print("aliza betageri")
print("my name is aliza")

#variables
name = "aliza"
age = 20
print(name)
print(age)
#string
name = "aliza"#name is a string variable
#string indexingstring indexing starts with 0 and ends with the last character
print(name[0])# prints a
print(name[1])# prints l
print (name[2])#prints i
print(name[3])#prints z
print(name[4])#prints a
#string slicing is the process of extracting a portion of a string using the slice operator [start:end] which starts with the starting index and ending index is excluded 

print(name[0:3])#prints ali
print(name[1:4])#prints liz
print(name[0:4])#prints aliz
print(name[0:5])#prints aliza
#negative indexing negative indexing starts with -1 and ends with the last character
print(name[-1])#prints a
print(name[-2])#prints z
print(name[-3])#prints i
print(name[-4])#prints l
print(name[-5])#prints a


#string length string length is the number of characters in a string and it can be calculated using the len() and strats with 1 and ends with the last charactes

print(len(name))#prints 5
print(len("aliza"))#prints 5
print(len("aliza betageri"))#prints 14
print(len("my name is aliza"))#prints 17

# string concatenation strong concatenation is the process of combining two or more strings into a single string using the + operator
first_name = "aliza"
last_name = "betageri"
full_name = first_name +" "+ last_name
print(full_name)#prints aliza betageri

#string built-in functions
#upper() function upper() function is used to convert a string to upppercase
name = "aliza"
print(name.upper())#prints ALIZA

#string capitalize() function capitalize() function is used to convert the first character of a string to uppercase and the rest of the characters to lowercase
name = "aliza"
print(name.capitalize())#prints Aliza

#string count() function count() function is used to count the number of occurrences of a substring in a sting 
name = "aliza betageri"
print(name.count("a"))#prints 3

#string find() function find() function is used to find the index of the first ouccurrence of a substring in a string and it returns -1 if the substring is not found 
#find the position of the character in the string
name = "aliza betageri"
print(name.find("a"))#prints 0
print(name.find("b"))#prints 6

#string replace() function replace() function is used to replace a substring in a sring with another substring 
name = "aliza betageri"
print(name.replace("a","A"))#PRINTS AlizA betAgeri

#string endwith()
name = "aliza betageri"
print(name.endswith("i"))#prints True
print(name.endswith("a"))#prints False

#input() fuction input() fuction is used to take input from the user and it returns a string 
name = input("enter your name: ")
print("hello "+name)
age = input("enter your age: ")
print("i am" + age + "years old")

#conditional statements 
age = 20
if age >=18:
    print("you are eligible to vote")

else:
    print("you are not eligible to vote")

#conditional statements with elif 
marks = int(input("enter your marks: "))
if marks >= 90:
    print("garde A")
elif marks >= 80:
    print("grade B")

elif marks >= 70:
    print("garde C")

else:
    print("garde D")

#odd and even numbers
number = int(input("enter a number:"))
if number % 2 == 0:
    print("even number")

else:
    print("odd number")

#greastest of three numbers
num1 = int(input('enter first number:'))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

if num1>=num2 and num1>=num3:
    print(num1,"is the greatest number")

elif num2>=num1 and num2>=num3:
    print(num2, "is the greatest number")

else:
    print(num3, "is the greatest number")
    
#lists
#list is a collection of items which are ordered and changeable and allows duplicate values and it is defined using square brackets []
students = [ "aliza", "betageri", "john", "doe"]
print((students))

marks = [90, 80, 70, 60, 50]
print(marks)

#indexing in lists is similar to string indexing and it starts with 0 and ends with the last character
marks = [90, 80, 70, 60, 50]
print(marks[0])#prints 90
print(marks[1])#prints 80
print(marks[2])#prints 70
print(marks[3])#prints 60
print(marks[4])#prints 50

#length of a list can be calculated using the len() function 
print(len(students))#prints 4
print(len(marks))#prints 5

#slicing in lists is similar to string slicing and it is used to extarct a portion of a list using the slice operator [start:end]
print(students[0:2])#prints ["aliza", "betageri"]
print(students[1:3])#prints ["betageri", "john"]
print(students[0:3])#prints ["aliza", "betageri", "john"]
#list methods
#append() method appened() method is used to add an item to the end of a list
students = ["aliza", "betageri", "john", "doe"]
students.append("jane")
print(students)#prints ["aliza", "betageri", "john", "doe", "jane"]

#insert() method insert() method is used to add an item at a specific index in a list 
students = ["aliza", "betageri", "john", "doe"]
students.insert(2,"jane")
print(students)#prints ["aliza", "betageri", "jane","john", "doe"]

#remove() method remove() method is used to remove an item from a list 
students = ["aliza", "betageri", "john", "doe"]
students.remove("john")
print(students)#prints ["aliza", "betageri", "doe"]

#pop() method pop() method is used to remove an item from a list at a specific index and it returns the removed item 
students = ["aliza", "betageri", "john", "doe"]
removed_item = students.pop(2)
print(removed_item)#prints john 

#sort() method sort() method is used to sort the items in a list in ascending order
marks = [90, 80, 70, 60,50]
marks.sort()
print(marks) #prints [50, 60,70 , 80, 90]

#descending order sort() method can also be used to sort the items in a list in descending order by passing the reverse = true argument to the sort()
marks = [90, 80, 95, 60, 100]
marks.sort(reverse = True)
print(marks)#prints [100, 95, 90,80, 60]

#reverse() method reverse() method is used to reverse the order of the items in a list 
marks = [90, 80, 70, 60, 50 ]
marks.reverse()
print(marks)#prints [50, 60, 70, 80, 90]

#tuple
#tuple is a collection of items which are ordered and unchangeable and allows duplicate values and it is defined using parentheses()
students = ("aliza", "betageri", "john", "doe")
print(students)#prints ("aliza", "betageri", "john", "doe")

#creating a tuple with one item requires a comma after the item to differentiate it from a regular parentheses
_single_item_tuple = ("aliza",) #note the comma after "aliza"
print(_single_item_tuple)#prints("aliza",)

#tuple methods
#count() method count() method is used to count the number of occurrences of an item in a tuple 
students = ("aliza", "betageri", "john", "doe", "aliza")
print(students.count("aliza"))#prints 2
#index() method index () method is used to find the index of the first occurrence of an item in a tuple 
print(students.index("aliza"))#prints 0
#practice questions 
#Store three favorite movies
movies = []
movie1 = input("enter your first favorite movie:")
movies.append(movie1)
movie2 = input("enter your second favorite movie:")
movies.append(movie2)
movie3 = input("enter your third favorite movie:")
movies.append(movie3)

print("Your favorite movies are:", movies)

#Palindrome
list = [ 1, 2, 3, 2, 1 ]

copy_list = list.copy()
copy_list.reverse()

if list == copy_list:
    print(list, "is a palindrome")
else:
    print(list,"is not a palindrome")


#sets
#set is a collection of items which are unordered , unchangeable ,and unindexed and it does not allow duplicate values and it is defined using curly braces {}
students = {"aliza", "betageri", "john", "doe"}
print(students)#prints {"aliza", "betageri", "john", "doe"}

#dictionaries
#dictionary is a collection of items which are unordered, changeable, and indexed and it does not allowed duplicte values and it is defined using curly braces {}
dictionary = {
    "name": "aliza",
    "age": 20,
    "city" : "addis ababa",
}
print(dictionary)
#accessing items in a dictionary is done using the key of the item
print(dictionary["name"])

print(dictionary["age"])
print(dictionary["city"])
print(dictionary.get("name"))

#nested dictionary is a dictionary that contains another dictionary as a value of one of its keys 
nested_dictionary = {
    "person1": {
        "name": "aliza",
        "age": 20,
        "city": "addis ababa",
    },
    "person2": {
        "name": "betageri",
        "age": 25,
        "city": "addis ababa"
    },
    "person3": {
        "name": "john",
        "age": 30,
        "city": "new york"
    }
}
print( nested_dictionary)
#loops 
#while loop is used to execute a block of code as long as a condition is true
count = 0
while count <= 5:
    print(count)
    count = count + 1

i = 1
while i <= 5:
    print(i)
    i += 1

#negative while loop 
count = 5
while count >= 0:
    print(count)
    count = count - 1
#while loop with break statement is used to exit the loop when a certain condition is met 
count = 0 
while count <= 5:
    print(count)
    if count == 3:
        break
    count = count + 1#prints 0 1 2 3

#while loop with continue statement is used to skip the current iteration of the loop when a certain condition is met
count = 0
while count <= 5:
    count = count + 1
    if count == 3:
        continue
    print (count)#prints 1 2 4 5 6
# program 
numbers = [1, 2, 3, 4, 5] 
index = 0                 #i = 0
while index < len(numbers): #while i<= 5
    print(numbers[index])#print(i)
    index = index+ 1#i = i + 1

n = int(input("Enter number: "))

i = 1

while i <= 10:
    print(n * i)
    i += 1
#Search in Tuple

nums = (3 , 6, 9, 12, 15, 18)

x= 12

i = 0
while i < len(nums):
    if nums[i] == x:
        print("found")
    i = i+1

#for loop 
fruits = ["apple", "mango", "banana", "strawberry"]

for fruit in fruits:
    print(fruit)

num1 = [2, 4, 8, 12, 16]
for nums in num1:
    print(nums)

nums = (1, 4, 8, 12, 16)
x = 16
for num in nums:
    if num == x:
        print("found")

#range
for i in range(1, 101):
    print(i)
for i in range (101, 1, -1):
    print(i)
#Print list in one line

def print_list(list):
    for items in list:
        print(items)

numbers = [1 ,2 ,3 ,4]
print_list(numbers)
#Factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
        print(fact)

factorial(5)
factorial(6)
#Length of List
def my_list(list):
    print(len(list))

my_list([10, 20, 30, 40])
def list_length(list):
    print(len(list))
list_length([10, 20, 30])
#USD to INR
def usd_to_inr(usd):
    print(usd * 83 )
usd_to_inr(10)
#Recursive Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
#oop 
class Student:
    def __init__(self, name, science, maths, english):
        self.name = name
        self.science = science
        self.maths = maths
        self.english = english

    def average(self):
        avg = (self.science+self.maths+self.english)/3
        print("average", avg)

s1 = Student("aliza", 70, 80,90)
s1.average()
#Create an Account class with 2 attributes — balance and account_no. Create methods for debit, credit, and printing the balance
class Account:
    def __init__(self, balance, account_no):
        self.__balance = balance
        self.account__no = account_no

    def debit(self, amount):
        if amount <= 0:
            print("invalid amount")
        elif amount > self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= amount

    def credit(self, amount):
        if amount <= 0:
            print("invalid amount")
        else:
            self.__balance += amount
    def print_balance(self):
        print("Balance:", self.__balance)
 #1. Start
#2. Input the list of exam scores
#3. n ← length of the list
#4. total ← 0
##5. For each score in the list:
      # total ← total + score
#6. average ← total / n
#7. If average ≥ 40:
 #      Return "Pass"
  # Else:
#Return "Fail"
#8. Stop

scores = [70, 80, 90, 60, 50]
n = len(scores)
total = 0
for score in scores:
    total += score
average = total / n
if average >= 40:
    print ("pass")
else:
    print("fail")

#using functionsresult = check_pass_fail([70, 80, 90, 60, 50])
#print(result)
def check_pass_fail(scores):
    n = len(scores)
    total = sum(scores)
    average = total / n
    if average >= 40:
        return "Pass"
    else:
        return "Fail"

result = check_pass_fail ([70, 80, 90, 60,50])
print(result)
