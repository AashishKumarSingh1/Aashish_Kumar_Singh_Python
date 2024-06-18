import math

what = input("Enter 'Area' to calculate Area and 'Volume' to calculate Volume: ")
shape = int(input("""
1) Enter 1 for Square
2) Enter 2 for Rhombus
3) Enter 3 for Pentagon
4) Enter 4 for Hexagon
5) Enter 5 for Heptagon
6) Enter 6 for Octagon
7) Enter 7 for Trapezoid
8) Enter 8 for Sphere
9) Enter 9 for Hemisphere
10) Enter 10 for Cone
11) Enter 11 for Cuboid
Enter your choice: """))

if what.lower() == "area":
    if shape == 1:
        side = float(input("Enter the side of the square: "))
        area = side * side
        print(f"The area of the square is: {area:.2f}")
    
    elif shape == 2:
        diagonal1 = float(input("Enter the first diagonal length: "))
        diagonal2 = float(input("Enter the second diagonal length: "))
        area = 1/2 * (diagonal1 * diagonal2)
        print(f"The area of the rhombus is: {area:.2f}")
    
    elif shape == 3:
        side = float(input("Enter the side length of the pentagon: "))
        area = (1/4) * 5 * (side ** 2) * (1 / math.tan(math.pi / 5))
        print(f"The area of the pentagon is: {area:.2f}")
    
    elif shape == 4:
        side = float(input("Enter the side length of the hexagon: "))
        area = (3 * math.sqrt(3) / 2) * (side ** 2)
        print(f"The area of the hexagon is: {area:.2f}")
    
    elif shape == 5:
        side = float(input("Enter the side length of the heptagon: "))
        area = (7/4) * (side ** 2) * (1 / math.tan(math.pi / 7))
        print(f"The area of the heptagon is: {area:.2f}")
    
    elif shape == 6:
        side = float(input("Enter the side length of the octagon: "))
        area = 2 * (1 + math.sqrt(2)) * (side ** 2)
        print(f"The area of the octagon is: {area:.2f}")
    
    elif shape == 7:
        base1 = float(input("Enter the length of the first base of the trapezoid: "))
        base2 = float(input("Enter the length of the second base of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        area = 1/2 * (base1 + base2) * height
        print(f"The area of the trapezoid is: {area:.2f}")
    
    # Add more shapes as needed with their respective formulas
    
    else:
        print("Invalid shape selection.")
        
elif what.lower() == "volume":
    if shape == 8:
        radius = float(input("Enter the radius of the sphere: "))
        volume = (4/3) * math.pi * (radius ** 3)
        print(f"The volume of the sphere is: {volume:.2f}")
    
    elif shape == 9:
        radius = float(input("Enter the radius of the hemisphere: "))
        volume = (2/3) * math.pi * (radius ** 3)
        print(f"The volume of the hemisphere is: {volume:.2f}")
    
    elif shape == 10:
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        volume = (1/3) * math.pi * (radius ** 2) * height
        print(f"The volume of the cone is: {volume:.2f}")
    
    elif shape == 11:
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        volume = length * width * height
        print(f"The volume of the cuboid is: {volume:.2f}")
    
    # Add more shapes as needed with their respective volume formulas
    
    else:
        print("Invalid shape selection.")
        
else:
    print("Invalid input. Please enter 'Area' or 'Volume'.")

print("Done!")
