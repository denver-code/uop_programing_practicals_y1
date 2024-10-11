import math

def biscuitCutting():
    number_to_cut = int(input("Please enter the number of biscuits to be cut: "))
    
    radius_of_biscuit = float(input("Please enter the radius of each biscuit [cm]: "))
    
    mixture_length = radius_of_biscuit * number_to_cut * 2
    mixture_width = radius_of_biscuit * 2

    # Improvisation out of available data
    area_of_mixture = mixture_length * mixture_width
    area_of_biscuit = math.pi * radius_of_biscuit ** 2
    
    total_area_of_biscuits = area_of_biscuit * number_to_cut
    waste_mixture = area_of_mixture - total_area_of_biscuits
    
    print(f"The width of the biscuit mixture is {mixture_width:.2f} cm.")
    print(f"The length of the biscuit mixture is {mixture_length:.2f} cm.")
    print(f"The area of the biscuit mixture is {area_of_mixture:.2f} cm².")
    print(f"The unused area of the mixture is {waste_mixture:.2f} cm².")

biscuitCutting()
