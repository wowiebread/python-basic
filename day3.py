#booleans
print(10 > 9) #is this true or false?
#booleans are used to evaluate expressions and conditions in python
# they are used to check if an expression is true or false
broughtFood = True
print(broughtFood)


is_raining = True
if is_raining:
    print("Take an unbrella!")
else:
    print("No umbrella needed")



temperature = 35
if temperature > 30:
    print("It's Warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's Cold")
print("Done")


age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

message = "Eligible" if age >= 18 else "Not eligible"
print(message)