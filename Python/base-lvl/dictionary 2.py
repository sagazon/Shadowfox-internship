my_expenses = {"Hotel":1500,
               "Food":1000,
               "Transportation":500,
               "Attractions":200,
               "Miscellaneous":100}

partner_expenses = {"Hotel":1200,
                    "Food":900,
                    "Transportation":700,
                    "Attractions":400,
                    "Miscellaneous":150}

my_total = sum(my_expenses.values())
print("my total expenses:",my_total)
partner_total = sum(partner_expenses.values())
print("partner's total expenses:",partner_total)

if my_total > partner_total:
    print("I spent more than my partner = ",my_total - partner_total)
elif partner_total > my_total:
    print("my partner spent more than me = ",partner_total - my_total)
else:
    print("me ans my partner spent the same amount.")

max_difference = 0
significant_category =""
for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        significant_category = category
print("category with the biggest difference:",significant_category)
print("difference amount:",max_difference)
    
               
