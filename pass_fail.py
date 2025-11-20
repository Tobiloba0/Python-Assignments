correct = 0
fail = 0


for student in range(10):
    user_input = int(input("Enter result(1 = pass, 2 = fail):"))

    if user_input == 1:
        correct = correct + 1
    elif user_input == 2:
        fail = fail + 1
    else:
        print("Enter a valid number. ")
print("The number of passes is ", correct, "and the number of failure is", fail)

if correct > 8:
    print("Bonus to faclitator")
else: print("Zero to facilitator")

    
