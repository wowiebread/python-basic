print("Hello Wolrd")
#print is a function that prints out a message to the console
#strings are surrounded by quotes
#singles or double quotes '' or ""
# whenever a word is surrounded by quotes it is called a string
# be consistent with the quotes you use
print("Your Name")
print("Order of Execution")
print("In Python")
print("*"*20)
#variables are used to stores data
#variables are created when you assign a value to it
#variables are case sensitive
price=10 #integer variable
name="John" #string variable
rating=4.9 #float variable
is_published= True #boolean variable
#start all variables with a lower case letter or underscore
print(name)
print(price)
print(rating)
#string interpolation where you can use variables in a sentence
print(name + "is a basketball player")
# concetentation to join variables in a sentence using
# the plus (+) sign
print(name + "has a rating of" +str(rating))
#use the str() function to convert a number to a string
# this is called type conversion
print("the price of the book is") + str(price)
# getting input from the user

name=input("What is your name")
age=input("What is your age")
occupation=input("What is your occupaiton?")
print("Hello" + name + "you are" + age "years old and you are a" + occupation)
