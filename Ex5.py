def factorial(x):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)

x = int(input("Enter a Number: "))
if x < 0:
    print("Factorial cannot be found for negative numbers")
elif x == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", x, "is: ", factorial(x))
