import math

def circumference(radius):
    return 2 * math.pi * radius

radius = float(input("Enter the radius: "))
print(f"Circumference: {circumference(radius):.4f}")