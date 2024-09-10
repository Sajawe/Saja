import math

# Function to compute distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Get user input for the coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the distance
dist = distance(x1, y1, x2, y2)

# Print the result formatted to 3 decimal places
print(f"The distance between ({x1:.1f},{y1:.1f}) and ({x2:.1f},{y2:.1f}) is {dist:.3f}")
