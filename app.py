# Welcome message
print("Welcome to my Python program!")

# Ask the user for input
hours = input("How many hours did you study today? ")

# Convert input safely with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Perform calculation
weekly_hours = hours * 7

# Display the result
print(f"You are on track to study {weekly_hours} hours this week.")