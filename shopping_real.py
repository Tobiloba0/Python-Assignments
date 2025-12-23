from datetime import datetime

#input_legit_number

def get_legit_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            user_input = int(value)
            if user_input <= 0:
                print("Value cannot be zero or less. Try again!!")
                continue
            return user_input
        except ValueError:
            print("Enter a valid whole number")


def get_legit_double(prompt):
    while True:
        value = input(prompt).strip()
        try:
            user_input = float(value)
            if(user_input < 0):
                print("Value cannot be zero or less. Try again!!")
            return user_input
        except ValueError:
            print("Enter a valid number")

def get_legit_letter(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("User input cannot be empty")
            continue
        return value


#creating invoice 

def print_invoice(date, time, customer_name, items, quantities, prices, discount, cashier_name):
    print(f"""
SEMICOLON STORES
MAIN BRANCH 
LOCATION: 312, HERBERT MACUALY WAY, SABO YABA, LAGOS.
TEL: 081348398238
Date: {date} Time: {time}
Cashier: {cashier_name}
Customer Name: {customer_name}  

""")

    print("=" * 65)
    print(f"{'':15} {'ITEM':15} {'QYT':10} {'PRICE':12} {'TOTAL(₦)':15}")
    print("-" * 65)

    sub_total = 0

    for index in range(len(items)):
        item_total = quantities[index] * prices[index]
        sub_total += item_total
        print(f"{'':15} {items[index]:8} {quantities[index]:10d} {prices[index]:11.2f} {item_total: 13.2f}")

    discount_value = (discount / 100) * sub_total
    vat = 0.0175 * (sub_total - discount_value)
    bill_total = sub_total - discount_value + vat

    print("_" * 65)
    print(f"{'':15} {'Sub Total:':15} {sub_total:15.2f}")
    print(f"{'':15} {'Discount:':15} {discount_value:15.2f}")
    print("=" * 65)

    return sub_total

def amount_paid(prompt, bill_total):
    while True:
        value = input(prompt).strip()
        try:
            amount = float(value)
            if amount < bill_total:
                print("Insufficient amount. Try again!!")
                continue
            print("Payment successful.")
            return amount
        except ValueError:
            print("Invalid value. Value must be a number!!")

# printing receipt
def print_receipt(date, time, customer_name, items, quantities, prices, discount, cashier_name, sub_total, amount_paid_value):

    print(f"""
SEMICOLON STORES
MAIN BRANCH 
LOCATION: 312, HERBERT MACUALY WAY, SABO YABA, LAGOS.
TEL: 081348398238
Date: {date} Time: {time}
Cashier: {cashier_name}
Customer Name: {customer_name}  

""")

    print("=" * 65)
    print(f"{'':15} {'ITEM':15} {'QYT':10} {'PRICE':12} {'TOTAL(₦)':15}")
    print("-" * 65)

    for index in range(len(items)):
        item_total = quantities[index] * prices[index]
        print(f"{'':15} {items[index]:8} {quantities[index]:10d} {prices[index]:11.2f} {item_total: 13.2f}")

    discount_value = (discount / 100) * sub_total
    vat = 0.0175 * (sub_total - discount_value)
    bill_total = sub_total - discount_value + vat
    balance = amount_paid_value - bill_total

    print("_" * 65)
    print(f"{'':15} {'Sub Total:':15} {sub_total:15.2f}")
    print(f"{'':15} {'Discount:':15} {discount_value:15.2f}")
    print(f"{'':15} {'VAT @ 17.50%:':15} {vat:15.2f} ")

    print("-" * 65)
    print(f"{'':16} {'Bill Total:':15} {bill_total:14.2f}")
    print(f"{'':16} {'Amount Paid:':15} {amount_paid_value:14.2f}")
    print(f"{'':16} {'Balance:':15} {balance:14.2f}")
    print("=" * 65)
    print("               THANK YOU FOR YOUR PATRONAGE")

    print("=" * 65)

# main method

def main():
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    items = []
    prices = []
    quantities = []

    customer_name = get_legit_letter("What is the customer's name?:")

    while True:
        item = get_legit_letter("What dis the user buy?:")
        qty = get_legit_int("How many pieces?: ")
        price = get_legit_double("How much per item?:")

        items.append(item)
        quantities.append(qty)
        prices.append(price)

        choice = input("Would you like to continue (yes / no)?:")
        if choice != "yes":
            break
    
    cashier_name = get_legit_letter("What is your name?:")
    discount = get_legit_int("How much discount will he get?: ")

    sub_total = print_invoice(date, time, customer_name, items, quantities, prices, discount, cashier_name)

    amount = amount_paid("How much did the customer give to you?: ", sub_total)

    print_receipt(date, time, customer_name, items, quantities, prices, discount, cashier_name, sub_total, amount)

#run
if __name__ == "__main__":
    main()

                
