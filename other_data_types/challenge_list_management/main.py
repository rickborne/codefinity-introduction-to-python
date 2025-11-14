#  1
meat = ['Ham', 3.99, 50, 'Sliced']
cheese = ['Chedder', 5.49, 100, 'Sharp']
condiment = ['Mustard', 1.99, 75, 'Spicy']
#2 &3
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)
if ('Ham' in deli_dept[0][0]) and (deli_dept[0][2] < 100):
    deli_dept[0][2] = 100
#4
seasonal_meat = ['Turkey', 4.50, 100, 'Sliced'] 
deli_dept.append(seasonal_meat)
#5
deli_dept.remove(condiment)
#6
deli_dept.sort()
#7
print("Updated Deli List:", deli_dept)