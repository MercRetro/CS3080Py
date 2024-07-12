import math

def cylinder_area(radius):
    height = 5
    # Calculate the surface area of the cylinder
    area = 2 * math.pi * radius * (radius + height)
    return area

# Example usage
radius_value = float(input("Enter the radius of the cylinder: "))
cylinder_surface_area = cylinder_area(radius_value)
print(f"The surface area of the cylinder with radius {radius_value} and height 5 is: {cylinder_surface_area:.2f}")
