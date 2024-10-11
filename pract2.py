"""
Code for programing (M30299-2024/25) practical session number 1
"""
from math import pi, sqrt, radians, sin, cos


def square_root_calculator():
    """
    Calculate square root of the number
    """
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers.")
    else:
        sqrt_value = sqrt(num)
        print("Square root:", round(sqrt_value, 2))


def sine_and_cosine():
    """
    Get Sine and Cosine of the angle
    """
    angle = float(input("Enter an angle in degrees: "))
    angle_in_radians = radians(angle)  # converts degrees to radians
    sine_value = sin(angle_in_radians)
    cosine_value = cos(angle_in_radians)
    print("Sine of the angle:", round(sine_value, 2))
    print("Cosine of the angle:", round(cosine_value, 2))

def speed_calculator():
    """
    Write a function speed_calculator that asks the user for two integers:
        1. the distance travelled in km (kilometres) 
        2. the duration of the journey in hours. 
    
    speed_calculator should then output the average speed in kilometres per hour (km/h).
    """
    distance = int(input("Please enter distance travelled [km]:"))
    duration = int(input("Please enter duration of travel [hours]:"))

    print(
        f"Average speed: {distance/duration} km/h"
    )


def circumference_of_circle():
    """
    Write a function circumference_of_circle that asks the user for the radius of a circle.
    The function should then output (print) the circle's circumference.
    Use the following formula. π is the pi constant from the math module,
    which you should import at the top of pract2.py.
    """
    radius = float(input("Please enter radius of the circle:"))

    circumference = 2 * pi * radius

    print(f"Circumference of circle: {circumference}")


def area_of_circle():
    """
    Write a function area_of_circle that asks the user for the radius 
    of a circle. It should then output the circle's area. 
    """
    radius = float(input("Please enter radius of the circle:"))

    area = pi * radius ** 2

    print(area)


def cost_of_pizza():
    """
    Write a function cost_of_pizza that asks the user for:
        1. diameter of a pizza (in cm).
    
    Your function should then output the cost of the pizza (based on its area) in pounds.
    Assume that the cost of the ingredients is 3.5 pence per square cm.
    """
    diameter = float(input("Please enter diameter of the pizza [cm]:"))

    pizza_area = pi * (diameter/2) ** 2
    print(f"Price of pizza: £{(pizza_area * 0.035):.2f}")


def slope_of_line():
    """
    Write a function slope_of_line that first asks the user for four values:
        x_1, y_1, x_2 and y_2 
    that represent two points in two-dimensional space 
    (i.e. points with coordinates (x_1, y_1) and (x_2, y_2)). 
    
    The function should then output the slope of the line that connects them.
    """
    x_1 = int(input("x1:"))
    y_1 = int(input("y1:"))

    x_2 = int(input("x2:"))
    y_2 = int(input("y2:"))

    slope = (y_2 - y_1) / (x_2 - x_1)

    print(f"Slope of the line: {slope}")


def travel_statistics():
    """
    Write a function travel_statistics which asks the user to input :
        1. average speed (in km/hour)
        2. duration (in hours) of a car journey. 
    
    The function should then output the overall distance travelled (in km),
    and the amount of fuel used (in litres) assuming a fuel efficiency of 5 km/litre.
    """
    speed = int(input("Please enter speed [km/h]:"))
    duration = int(input("Please enter duration [hours]:"))

    distance = speed * duration

    fuel_consumed = distance / 5

    print(f"Your car consumed {fuel_consumed} litres of fuel for {distance}km")


def sum_of_squares():
    """
    Write a function sum_of_squares that uses a loop to output the sum 12 + 22 + … + n2
    where n is an integer provided by the user.  
     
    For example, if the user enters 3, the function should output 14 (12 + 22 + 32).
    """
    sum_of_numbers = 0
    n = int(input("N:"))

    for i in range (1, n+1):
        sum_of_numbers += i**2

    print(sum_of_numbers)


def average_numbers():
    """
    Write a function average_of_numbers which outputs the average of a series of number
    entered by the user. 
    
    The function should first ask the user how many numbers there are to be inputted
    """
    numbers_amount = int(input("How many numbers would you like to process:"))

    sum_of_numbers = 0

    for i in range(1, numbers_amount+1):
        sum_of_numbers += int(input(f"Please enter the number {i}:"))
    print(f"The average of numbers: {sum_of_numbers/numbers_amount}")


def fibonacci_sequence():
    """
    [harder] Write a function fibonacci which asks the user for a number n.
    Use a loop to calculate and output the nth value in the Fibonacci sequence.
    """
    n = int(input("N:"))

    num1 = 0
    num2 = 1

    next_number = num2

    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2


def select_coins():
    """
    Write a function select_coins that asks the user an amount of money in pence.
    It should output the number of coins of each denomination (£2 to 1p)
    that should be used to make up that amount.  
    For example, if the input is 292 pence, then the function should report the following: 
    1 x £2, 0 x £1, 1 x 50p, 2 x 20p, 0 x 10p, 0 x 5p, 1 x 2p, 0 x 1p
    """
    amount = int(input("Please enter amnount of poney in pence:"))

    coins = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
        "5p": 5,
        "2p": 2,
        "1p": 1
    }

    for item, value in coins.items():
        count = amount // value

        print(f"{count} x {item}")

        amount %= value


def select_coins_2():
    """
    Same as select_coins but using lists
    """
    amount = int(input("Please enter amnount of poney in pence:"))

    coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
    coin_names = ["£2","£1", "50p", "20p", "10p", "5p", "2p", "1p"]

    coin_counts = []

    for i in coin_values:
        count = amount // i
        coin_counts.append(count)
        amount %= i

    for name, count in zip(coin_names, coin_counts):
        print(
            f"{count} x {name}"
        )
