

#product_name = input("Enter name of item: ")
#original_price = int(input("Enter the price of the item: "))
#promotional_code = input("Enter the promo code: ");
#
print(product_details(500))


def product_details(produdct_name, original_price, promotional_code):


    if promotional_code == SAVE10:
        product_price -= 0.01 * original_price;
    elif promo_code == HALFOFF:
        product_price -= 0.50 * original_price;
    else: product_price = original_price; 

    return product_price

