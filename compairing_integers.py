#compairing integers

print("Enter two integers and I will tell you the relationship they satisfy.")

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))

if number_one != number_two:
    print(number_one, "is not equal to ", number_two)
elif number_one < number_two:
    print(number_one, "is less than ",number_two)
else:
    print(number_one, "is equals to ", number_two)
