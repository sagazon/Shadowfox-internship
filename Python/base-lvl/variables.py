# pi and checking its type
pi = 22 / 7
print(type(pi))

print('\n')

# Input principal amount(P), rate of interest(T), and time(T)
P = int(input("Enter the principal amount: "))
R = int(input("Enter the rate of interest in %: "))
T = 3  # Fixed time in years

# Calculating simple interest
simple_interest = (P * R * T) / 100
print("Simple interest for", T, "years is", simple_interest)


