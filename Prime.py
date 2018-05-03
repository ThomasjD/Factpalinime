#Determine if a number is a prime number

#user input
number = int(input("Enter an integer."))
small_prime = [2,3,5,7]
prime = True

if number > 10:
    for x in range(2, 9):
        if number%x == 0:
            prime = False
else:
    for x in small_prime:
        if number == x:
            prime = True
            print("yes")
        else:
            prime = False

if prime == True:
    print (f"The number {number} IS a prime number.")
else:
    print (f"The number {number} is NOT a prime number.")
