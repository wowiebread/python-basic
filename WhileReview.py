# While loops allow you to repeat code until a condition is met
# While loops are defined with the while keyword
# While loops are used when you don't know how many times you need to repeat the code

studentList = ("Citlalic", "Praise", "Aaron", "Fiona", "Xavier")
studentName = 0
while studentName < len(studentList):
   print(studentList[studentName])
   studentName += 1

fruitList = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# for loop to print the fruitList
# for loop is when you know how many times you need to repeat the code
for fruit in fruitList:
   print(fruit + " is a fruit.")

studentList = ("Citlalic", "Praise", "Aaron", "Fiona", "Xavier")

for student in studentList:
    ask = input("What is your last name?")
    print(student + "" + ask)