# app.py
# -------------------------------------------
# Gym Time Calculator Program
# This program asks the user how many hours
# they plan to go to the gym per day and
# calculates their total weekly gym hours.
# Includes error handling for invalid input.
# -------------------------------------------

print("Welcome to the Gym Time Calculator!")

# Ask the user for input
hours = input("How many hours do you plan to go to the gym today? ")

try:
    # Convert input to float
    hours = float(hours)
except ValueError:
    print("Error: Please enter a valid number for gym hours.")
    exit()

# Perform calculation
weekly_hours = hours * 7

# Display results
print(f"\nIf you keep this pace, you will spend {weekly_hours} hours at the gym this week!")

# Program finalized with comments + cleanup