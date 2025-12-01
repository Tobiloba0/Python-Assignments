
user_input = int(input("Enter a number: "))

factorial = 1


for count in range(1, user_input + 1):
    factorial *= count

print("The factorial of", user_input, "is:", factorial)

