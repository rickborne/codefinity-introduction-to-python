#You need to define a variable for the total cost, create a boolean variable to check for discount
#eligibility, and print the result.

# Define a variable named total_cost and assign it the value 25.00 to represent the total cost of a
#grocery bill.
# Create a boolean variable named discountEligible by comparing the total_cost variable to the
#discount threshold of 20.00 using the greater than or equal to (>=) operator.
# Print the value of the discountEligible variable to indicate whether the purchase is eligible for
#a discount.
# Output Requirements
# Print the message: Is the purchase eligible for a discount? <discountEligible>.

total_cost = 25.00
discount_threshold = 20.00
discountEligible = total_cost >= discount_threshold
print("Is the purchase eligible for a discount?", discountEligible)
