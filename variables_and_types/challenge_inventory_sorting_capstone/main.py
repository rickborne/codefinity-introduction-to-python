# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slicing Items
candy1 = items[0:9]
candy2 = items[11:20]
print(candy2)
dry_goods = items[22:]

# Slicing Categories
category1 = categories[0:12]
category2 = categories[13:]

# Price Variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print("We have", candy1,"for", bubblegum_price,"in the", category1) 
print("We have", candy2,"for", chocolate_price,"in the", category1)
print("We have", dry_goods,"for", pasta_price,"in the", category2)