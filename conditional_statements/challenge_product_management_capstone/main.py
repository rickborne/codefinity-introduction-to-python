# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"
is_perishable = ""
# Decision making
if type(product_type) == str and type(stock_level) == int and type(days_until_expiration) == int: 
    if product_type == "Perishable":

        if  stock_level > 50:
            # 30% discount if expires in 3 days_until_expiration
            if days_until_expiration < 4 and stock_level > 50:
                print("30% discount applied")
            
            # 20% discount if expires in 4-6 days_until_expiration
            elif (days_until_expiration>3) and (days_until_expiration<7):
                print("20% discount applied")
            else:
                end
        # 10% discount if expires in 7+ days_until_expiration
        elif  stock_level <= 50 and days_until_expiration > 6:
            print("10% discount applied")
        # No discount otherwise
        else:
            print("No discount available for non-perishable items.")
    else:
        print("No discount available for non-perishable items.")
else:
    print("Your product type needs to be of type string, and your stock level and days of expiration need to be integers")