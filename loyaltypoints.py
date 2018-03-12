#!?usr/bin/python
import sys, traceback
import sys
from sys import exit
import sqlite3 
from sqlite3 import Error

person =[]
age =[]
email =[]
quality_points = 0

conn = sqlite3.connect('loyalty_points.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS customers(person, age, email, quality_points)''' )
#c.execute("INSERT INTO customers (person, age, email, quality_points)VALUES (?, ?, ?, ?)", (person, age, email, quality_points))
conn.commit()

print("Welcome to Joey's Loyalty and Rewards Program")
name = input('Please enter your first and last name: ')
person.append(name)

print('Hello', person, '!')
years_old = int(input("Please Enter your age: "))
age.append(years_old)

if years_old < 18:
    print("Sorry you are too young to join our rewards program :(")
    sys.exit()
elif years_old > 18: 
    print("""We are delighted you would like to be a member!""")
    
email_address = input("Please Enter your email: ")
email.append(email_address)

years = int(input("How many years have you been shopping with us?"))

if years >= 3:
    quality_points += years
elif years <= 2:
    print("Just a little longer and you'll earn quality points!")
    
print("We are so excited to have you as a customer")

items = int(input("How many reciepts do you have for purchace's made with us?"))
            
if items >= 20:
            quality_points += items
elif items <= 19:
            print("Just a few more items and you'll earn quality points")
survey = input("""Please complete this short survey on customer Service quality,
               if you perfer not to please enter no if you would like to type yes:   """)

if survey == "no":
            print("Alright, well thank you for your time. great day!")
            sys.exit()
elif survey == "yes":
            print("Alright Let's get started!")
        
            
            print("Have you enjoyed shopping at Hoodwink Enterprises?")
            answer1 = input()
            print("Is there anything we can change?")
            answer2 = input()
            print("Alright we'll get right on it")
            print("Did you enjoy your last visit with us?")
            answer3 = input()
            if answer3 == "no":
                print("We apologize and we promise our representives will make sure your next visit is great!")
            if answer3 == "yes":
                print("it's great to know we're doing well by our valued customers")
                print("You have completed the survey! Thank you for your time!!")
                print("You will be rewarded 10 loyalty points!!")
                quality_points += 10
            
c.execute("INSERT INTO customers (person, age, email, quality_points)VALUES (?, ?, ?, ?)", (name, years_old, email_address, quality_points))
conn.commit()
