
#Enter number
number = int(input("Enter an intenger"))

#Calculation
num = 1
for x in range(1, number + 1):
    num = x * num

#Display
print(f"The Factorial of {number} is {num}. ")
