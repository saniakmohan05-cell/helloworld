# class Student:
#     def__init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Sania",20)
# print("name",s1.name)
# print("age",s1.age)



# class Animal:
#     def sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# d=Dog()
# d.sound()
# d.bark()


# polymorphism...
# class Bird():
#     def sound(self):
#         print(" Bird Make sound")
# class Cat():
#     def sound(self):
#         print("Cat Make sound")
# b=Bird()
# c=Cat()
# b.sound()
# c.sound()  

# Encapsulation...
# class Bank():
#     def __init__(self):
#         self._balance=1000
#     def show_balance(self):
#         print(self._balance)
# b=Bank()
# b.show_balance()


# # Abstraction...
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class square(shape):
#     def area(self):
#         print("Area of square")
# s=square()
# s.square()                
