#!/bin/python3

# list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Calculating the members
members = len(justice_league)
print("Number of members in the Justice League:",members)

# Add Batgirl and Nightwing to the list
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

# Moveing Wonder Woman to the frist place 
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# Moveing Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
justice_league.insert(3, "Green Lantern")
print("After adding Green Lantern between Aquaman and Flash:", justice_league)

# New team members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After assembling the new team:", justice_league)

# Sort the Justice League alphabetically and make the 0th index the new leader
justice_league.sort()
print("After sorting alphabetically:", justice_league)
print("New leader of the Justice League:", justice_league[0])

