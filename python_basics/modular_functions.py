#Task 3: Writing Modular Python Code
import math
def calculate_area(shape, dimension1, dimension2=0):
    shape = shape.lower()
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Wrong input"

print("Circle area:", calculate_area("circle", 5))
print("Rectangle area:", calculate_area("rectangle", 4, 6))
print("Triangle area:", calculate_area("triangle", 3, 8))
print("Error test:", calculate_area("square", 3, 8))

