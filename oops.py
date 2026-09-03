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


class Student:
    college = "ABC College"   # class variable — defined directly inside the class, outside any method

    def __init__(self, name):
        self.name = name       # instance variable — belongs to each individual object
s1 = Student("aliza")
s2 = Student("karan")

print(s1.name, s1.college)   # aliza ABC College
print(s2.name, s2.college)   # karan ABC College
class car:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand 
car1 = car("toyata")
car2 = car("honda")
car3 = car("ford")
print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)
print(car3.brand, car3.wheels)

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)

class Employee:
    company = "techcropt"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def raise_salary(self, amount):
        self. salary += amount
Employee1 = Employee("Alice", 50000)
Employee2 = Employee("Bob", 60000)
raise_amount = 5000
Employee1.raise_salary(raise_amount)
Employee2.raise_salary(raise_amount)
print(Employee1.name, "new salary:", Employee1.company, Employee1.salary)
print(Employee2.name, "new salary:", Employee2.company, Employee2.salary)

#Create a BankAccount class with:

#A class variable bank_name = "State Bank"
#A @classmethod called change_bank_name(cls, new_name) that updates bank_name
#A @staticmethod called is_valid_amount(amount) that returns True if amount > 0, else False

class BankAccount:
    bank_name = "state bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        return cls.bank_name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
BankAccount.change_bank_name("HDFC")
print(BankAccount.bank_name)
print(BankAccount.is_valid_amount(1000))
#Problem 1 — classmethod used as an alternative constructor (a very common real-world pattern):
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2026
        age = current_year - birth_year
        return cls(name, age)
s1 = Student.from_birth_year("aliza", 2006)
s2 = Student.from_birth_year("karan", 2008)

print(s1.name, s1.age)
print(s2.name, s2.age)

class Product:
    tax_rate = 0.18   # 18% tax, class variable

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * Product.tax_rate)

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    @staticmethod
    def is_valid_price(price):
        return price > 0

p1 = Product("Laptop", 1000)

print(p1.price_with_tax())        # Line A

Product.change_tax_rate(0.05)

print(p1.price_with_tax())        # Line B

print(Product.is_valid_price(-5)) # Line C

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e1 = Employee("Aliza", 50000)

print(e1.get_salary())     # Line A
#print(e1.__salary)         # Line B

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self._speed = speed   # protected

    def show_speed(self):
        return self._speed

v1 = Vehicle("Tesla", 120)

print(v1.brand)         # Line A
print(v1._speed)        # Line B
print(v1.show_speed())  # Line C

class Wallet:
    def __init__(self, amount):
        self.__amount = amount

    def __show(self):          # notice: this method itself is private too
        return self.__amount

    def public_check(self):
        return self.__show()   # calling the private method from INSIDE the class

w1 = Wallet(500)

print(w1.public_check())   # Line A
#print(w1.__show())         # Line B
class Employee:                    # parent class (also called "base class" or "superclass")
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):           # child class (also called "subclass" or "derived class")
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # calls Employee's __init__ to set up name & salary
        self.team_size = team_size
 
# create an instance of Manager
m1 = Manager("Aliza", 80000, 5)

print(m1.name)             # Line A
print(m1.salary)           # Line B
print(m1.team_size)        # Line C
m1.show_details()          # Line D

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        print(f"Manager: {self.name}, Team Size: {self.team_size}")

m1 = Manager("Aliza", 80000, 5)
m1.show_details()
#Scenario 1 (no override — Manager doesn't define show_details at all)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    # no show_details() here

m1 = Manager("Aliza", 80000, 5)
m1.show_details()
#Scenario 2 (override — Manager defines its own show_details):
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        print(f"Manager: {self.name}, Team Size: {self.team_size}")

m1 = Manager("Aliza", 80000, 5)
m1.show_details()
#Create a Vehicle class with __init__(self, brand) and a method show_info() that prints f"Brand: {self.brand}". Then create a Car class that inherits from Vehicle, adds a model attribute, and overrides show_info() to print both the brand and model — using super() to reuse the parent's print line instead of rewriting it.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        super().show_info()
        print(f"Model: {self.model}")

c1 = Car("Toyota", "Camry")
c1.show_info()

class vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show_info(self):
        print(f"Brand: {self.brand}")

class car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def show_info(self):
        super().show_info()
        print(f"model: {self.model}")
car1 = car("toyota", "camry")
car1.show_info()
#Problem 1 — what if __init__ is overridden but super().__init__() is forgotten?
class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = "some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed   # notice: super().__init__() is NOT called here

d1 = Dog("Rex", "Labrador")

print(d1.breed)    # Line A
#print(d1.name)     # Line B
#Create a Book class with attributes title and author. Add a method display() that prints "Title: X, Author: Y".
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
a1 = Book("the alchemist", "paulo coelho")
a2 = Book("the power of now", "Eckhart Tolle")

a1.display()
a2.display()
#Create a Rectangle class that takes length and width in the constructor. Add a method area() that returns the area, and a method perimeter() that returns the perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(5, 3)
print(r1.area())
print(r1.perimeter())

#Create a #Person class with name and age. Add a method is_adult() that returns True if age ≥ 18, else False.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

p1 = Person("Aliza", 20)
p2 = Person("Karan", 16)

print(p1.is_adult())  # True
print(p2.is_adult())  # False
#🟡 Level 2
#Create a Wallet class with a private attribute __balance. Add add_money(amount) and spend_money(amount) methods — both must reject negative or zero amounts, and spend_money must also reject if amount > balance.
class Wallet:
    def __init__(self):
        self.__balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount. Please enter a positive value.")

    def spend_money(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def get_balance(self):
        return self.__balance
b1 = Wallet()
b1.add_money(100)
b1.spend_money(150)
print(b1.get_balance())
b1.spend_money(-20)
print(b1.get_balance())
#Create a Library class where total_books is a class variable starting at 0. Every time a new Book object is created (constructor), increment total_books by 1. After creating 4 books, what does Library.total_books print?
class Library:
    total_books = 0

    def __init__(self):
        Library.total_books += 1
b1 = Library()
b2 = Library()
b3 = Library()
b4 = Library()
print(Library.total_books)

class Item:
    discount = 10   # class variable

    def __init__(self, price):
        self.price = price

i1 = Item(100)
i2 = Item(200)

i1.discount = 20         # Line 1
Item.discount = 15       # Line 2

print(i1.discount)       # ?
print(i2.discount)       # ?
#. Create an Account class where account_no is public, but __pin is private. Add a method verify_pin(entered_pin) that returns True/False. Then try accessing __pin directly from outside — what error do you expect, and why?
class Account:
    def __init__(self, account_no, pin):
        self.account_no = account_no
        self.__pin = pin 

    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin
a1 = Account("123456", "7890")
print(a1.verify_pin("7890"))  # True
# print(a1.__pin)  # This would raise an AttributeError
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing")

p1 = Puppy("Rex")
p1.eat()   # Inherited from Animal
p1.bark()  # Inherited from Dog
p1.play()  # Defined in Puppy

class A:
    def show(self):
        print("A's show")

class B(A):
    pass

class C(B):
    def show(self):
        print("C's show")

c1 = C()
c1.show()          # Line A

print(C.__mro__)   # Line B
class Flyer:
    def move(self):
        print("Flyer's move: flying")

class Swimmer:
    def move(self):
        print("Swimmer's move: swimming")

class Duck(Swimmer, Flyer):
    pass

d1 = Duck()
d1.move()
print(Duck.__mro__)
class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Circle area: {3.14 * self.radius ** 2}")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print(f"Square area: {self.side ** 2}")

shapes = [Circle(5), Square(4)]

for shape in shapes:
    shape.area()

class Robot:
    def speak(self):
        print("Beep boop")

class Human:
    def speak(self):
        print("Hello there")

things = [Robot(), Human()]

for thing in things:
    thing.speak()
    #1 — combining MRO with attribute values (not just methods):
class A:
    def __init__(self):
        self.value = "A's value"

class B(A):
    def __init__(self):
        super().__init__()
        self.value = "B's value"

class C(B):
    pass

c1 = C()
print(c1.value)

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    def show(self):
        print(f"{self.name}: ${self.calculate_pay()}")

class FullTime(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    def calculate_pay(self):
        return self.monthly_salary

class Freelancer(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
    def calculate_pay(self):
        return self.hours * self.rate

workers = [FullTime("Aliza", 50000), Freelancer("Karan", 100, 500)]

for w in workers:
    w.show()
#Create a Temperature class with:

#A private attribute __celsius
#A @property called celsius that returns the value
#A @celsius.setter that rejects any value below -273.15 (absolute zero — physically impossible temperature) and prints an error message in that case, otherwise updates it normally
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Error: Temperature below absolute zero is not possible.")
        else:
            self.__celsius = value

t1 = Temperature(25)
print(t1.celsius)      # Line A

t1.celsius = -300
print(t1.celsius)      # Line B

t1.celsius = 100
print(t1.celsius)      # Line C
#write the full Book class, with __init__ (taking title and author) and __str__ (returning "Harry Potter by J.K. Rowling" style output, using only self).
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b1 = Book("Harry potter", "j.k. rowling")
print(b1)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

b1 = Book("Harry Potter", "J.K. Rowling")

print(b1)              # Line A — uses __str__
print([b1, b1])         # Line B — a LIST containing the object — uses __repr__ instead!

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("Harry Potter", "J.K. Rowling")

print(b1 == b2)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("Harry Potter", "J.K. Rowling")

print(b1 == b2)   # now checks content instead of identity



class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

w1 = Wallet(100)
w2 = Wallet(50)
print(w1 + w2)

#aggeration
class Author:
    def __init__(self, name):
        self.name = name
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"title: {self.title}, Author: {self.author.name}")

a1 = Author("J.k. rowling")
b1 = Book("Harry potter", a1)
b1.display()
#based on __call__ printing f"Hello, {self.name}!", and g1 = Greeter("Aliza") — what do you think g1() prints?
class Greeter:
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print(f"Hello, {self.name}!")
        
g1 = Greeter("Aliza")
g1()  # This will print: Hello, Aliza!
class Dog:
    pass

print(type(Dog))
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class Dog(metaclass=MyMeta):
    pass
def remove_duplicates(numbers):
    slow_pointer = 0
    for fast_pointer in range(1, len(numbers)):
        # your logic here: compare numbers[slow_pointer] and numbers[fast_pointer]
        # if different: move slow_pointer forward, place the new value there
        if numbers[slow_pointer] != numbers[fast_pointer]:
            slow_pointer += 1
            numbers[slow_pointer] = numbers[fast_pointer]
    return numbers[:slow_pointer + 1]   # the unique portion of the list
       