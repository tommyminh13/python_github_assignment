print("Welcome to the Gym Time Calculator!")

hours = input("How many hours do you plan to go to the gym today? ")

try:
    # Convert input to float
    hours = float(hours)
except ValueError:
    print("Error: Please enter a valid number for gym hours.")
    exit()
    
weekly_hours = hours * 7

print(f"\nIf you keep this pace, you will spend {weekly_hours} hours at the gym this week!")