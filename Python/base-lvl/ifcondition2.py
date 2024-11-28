#!/bin/python3

# check if two cities belong to the same country
australia = ["sydney", "melbourne", "brisbane", "perth"]
uae = ["dubai", "abu dhabi", "sharjah", "ajman"]
india = ["mumbai", "bangalore", "chennai", "delhi"]

# city names from user input
city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()


if city1 in australia:
    country1 = "Australia"
elif city1 in uae:
    country1 = "UAE"
elif city1 in india:
    country1 = "India"
else:
    country1 = None

# Determine the country of the second city
if city2 in australia:
    country2 = "Australia"
elif city2 in uae:
    country2 = "UAE"
elif city2 in india:
    country2 = "India"
else:
    country2 = None

# Check if both cities belong to the same country
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")





