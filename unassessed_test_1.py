from math import pi


def biscuit_cutting():
    biscuit_diameter = float(input("Please enter the diameter of each biscuit [cm]: "))
    biscuits_along_length = int(input("Please enter the amount of biscuits along length: "))
    biscuits_along_width = int(input("Please enter the amount of biscuits along width: "))
    
    biscuit_radius = biscuit_diameter / 2
    biscuit_area = pi * biscuit_radius ** 2
    
    mixture_length = biscuit_diameter * biscuits_along_length
    mixture_width = biscuit_diameter * biscuits_along_width
    
    mixture_area = mixture_length * mixture_width
    
    total_biscuits = biscuits_along_length * biscuits_along_width
    biscuits_area = biscuit_area * total_biscuits
    
    spare_area = mixture_area - biscuits_area
        
    biscuits_can_be_made = spare_area // biscuit_area
    
    print(f"Radius of each biscuit: {biscuit_radius:.2f}cm")
    print(f"Area of each biscuit: {biscuit_area:.2f}cm^2")
    print(f"Total area of biscuit mixture (including spare): {mixture_area:.2f}cm^2")
    print(f"Biscuits can be made out of spare mixture: {biscuits_can_be_made}")
