# print ("Hello World")

'''Variables'''
# a=3
# a=32
# a=1
# print(a+a+a)

'''Data Types'''
#a=3.63844
# b=23
# c=True
# d="Happy Day"
# d1='12,3$$#&srA'
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(d1))

'''Type Conversion'''
#print(int(a))

'''Concatenation'''
#print("My " "name " + "is " + "Adwoa")

'''Examples'''
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# new_age=int(age) + 10
# print ("Your name is " + name + ". " + "You're " + str(new_age) + " years old.")
#fstring#
#print(f'Your name is {name}. You are {new_age} years old.')

'''Indexing and Slicing'''
# word="Helicopter"
# print(word[0])
# print(word[1])
# print(word[6])
# print(word[-1])
# print(word[0:4])
# print(word[3:])
# print(word[:3])

'''ask a user to enter any two digit number, take the number separate it and add it and return it to the user'''
# number=input("Enter a two number: ")
# num1=int(number[0])
# num2=int(number[1])
# result=num1 +num2
# print("The sum of each digit is " + str(result))

'''enter weight in kg, and height in metres and find bmi'''
# weight=float(input("Please enter your weight in kg: "))
# height=float(input("Please enter your height in m: "))
# bmi= weight/(height**2)
# print(f"Your BMI is {round(bmi,3)} kg/m^2")
# if bmi < 18: 
#     print("You're underweight.")
# elif bmi>=19 and bmi<=25:
#     print("You're weight is normal")
# elif bmi >25 and bmi<=30:
#     print("You're overweight")
# else:
#     print("You're obese")


'''Conditional Statements'''
# if 4==4:
#     print("That is correct")
# else:
#     print("That is wrong")

'''Determine if a number entered by a user is even or odd'''
# number=int(input("Enter a number: "))
# if number%2==0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

'''Randomisation-- Modules in py are like a toolbox, theyhave codes created for us and bundled together. '''
#import random
# dice_value=random.randint(1,6)
# print(dice_value)
'''Task on coinflipping probs'''
# coin_value=random.randint(0,1)
# print(coin_value)
# if coin_value==1:
#     print("Head")
# else:
#     print("Tail")

'''Lists'''
# fruits=["Apples","Mango","Orange","Peach","Grapes"]
# print(fruits[0:3])
# fruits.append("Pineapple")
# fruits.extend(["Melon","Banana"])
# print(fruits)

'''For Loop'''
# for i in range(2,11,2):
#     print(i)
# sum=0
# for number in range(1,101):
#     sum+=number
# print(sum)
'''Sum of even numbers from 2 to 100'''
# sum=0
# for number in range(2,101,2):
#     sum+=number
# print(sum)

'''While loop'''
# x=1
# while x !=100:
#     x+=1
#     print(x)

'''Functions'''
# def my_function(name, location):
#     print(f"Hello, I am {name},I am from {location}")
# my_function(location="Adwoa",name="Accra")

'''Dictionaries'''
'''OOP'''

