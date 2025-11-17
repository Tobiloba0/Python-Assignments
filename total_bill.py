total_bill = int(input(Enter total bill: ))

is_member = input(Enter yes if you are a member and no if you are not a member)

if (bill >= 1000 and is_member == "yes"):
    discount = 0.1 * total_bill

    member_bill = total_bill - discount

    print(member_bill)


elif: (total_bill >=1000 and is_member == "no"):
    discount = 0.05 * total_bill

    nonmember_bill = total_bill - discount
    print(nonmember_bill)

