total_bill = int(input(Enter total bill: ))

is_member = input(Enter yes if you are a member and no if you are not a member)

if total_bill >= 1000 and is_member == "yes":
    discount = 0.1 * total_bill
    discounted = total_bill - discount
    print(f"You are to pay the sum of {discounted}")

elif total_bill >=1000 and is_member == "no"):
    discount = 0.05 * total_bill
    discounted = total_bill - discount
    print("You are to pay the sum of ",discounted)

