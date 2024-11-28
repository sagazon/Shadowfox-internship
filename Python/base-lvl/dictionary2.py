#!/bin/python3

# My expenses 
my_expenses = {
    "Hotel": 2000,
    "Food": 3000,
    "Transportation": 1000,
    "Games": 1500,
    "Purchase": 2000
}

# Partner's expenses
partner_expenses = {
    "Hotel": 3000,
    "Food": 3500,
    "Transportation": 4000,
    "Visiting": 2000,
    "purchase": 3000
}


my_total = sum(my_expenses.values())
partner_total = sum(partner_expenses.values())

# Printing total expenses
print(f"My total expenses: {my_total}")
print(f"My partner's total expenses: {partner_total}")


if my_total > partner_total:
    print("I spent more money overall.")
elif my_total < partner_total:
    print("My partner spent more money overall.")
else:
    print("We both spent the same amount of money.")


largest_diff_category = ""
largest_diff_amount = 0

all_categories = set(my_expenses.keys()).union(set(partner_expenses.keys()))

for category in all_categories:
    my_expense = my_expenses.get(category, 0)  
    partner_expense = partner_expenses.get(category, 0)  
    
    diff = abs(my_expense - partner_expense)
    if diff > largest_diff_amount:
        largest_diff_category = category
        largest_diff_amount = diff

# Print the category with the largest difference
print(f"The category with the largest spending difference is '{largest_diff_category}' with a difference of {largest_diff_amount}.")

