#finding the factorial of a number

userInput = int(input("Enter a number: "));
factorial = 1

for count in range(1, userInput+1):
    factorial = factorial * count

print("The factorial of ", userInput, " is:", factorial)
