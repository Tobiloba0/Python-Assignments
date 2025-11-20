for year in range(30):
    deposit_amount = 1000 * (1 + 0.07) ** year
    print(f"The interest after {year + 1} year(s) is {deposit_amount:0.2f}")
    
