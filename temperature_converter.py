def temperature_checker(value, unit='C', cold_threshold=10, heat_threshold=30):
    """
    convert temperature from degrees to farenheit and from farenheit to degrees and also check their treshold based on the treshold provided.
    """

    if unit.upper() == 'C':
        converted = (value * 9/5) + 32
        new_value = 'F'
    elif unit.upper() == 'F':
        converted = (value - 32) * (5/9)
        new_value = 'C'
    else:
        raise ValueError("Unit must be 'C' or 'F'")

    celsius_value = value if unit.upper() == 'C' else converted

    if celsius_value <= cold_threshold:
        alert = "Cold advisory"
    elif celsius_value >= heat_threshold:
        alert = "Heat alert"
    else:
        alert = "Normal temperature"

    return converted, new_value, alert




def apply_discount(item_name, original_price, promo_code):
    if original_price < 0:
        raise ValueError("Value to low and cannot be less than 0")

    promo_code = promo_code.upper()

    if promo_code == "SAVE10":
        discount = original_price * 0.10
    elif promo_code == "HALFOFF":
        discount = original_price * 0.50
    else:
        discount = 0

    final_price = original_price - discount
    return round(final_price, 2)





