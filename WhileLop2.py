#loopps repeat a block of code multiple times
#while loop repeats a block of code as long as a condition is true
#For loop repeats a block of code a specific number of times

list1 = range(1,1001)
#print(list1)
for number in list1:
    if number % 2 == 0:
        print(f'Number is even: {number}')
    else:
        print("Odd Number is NOT even")

#sum
print(f'The sum of the list is {sum(list1)}')