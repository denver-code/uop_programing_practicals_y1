"""
Code for programing (M30299-2024/25) practical session number 1
"""


def say_name():
    """
    Write a function called say_name that displays your name. 
    """
    print("Ihor")


def say_hello_2():
    """
    Write a say_hello_2 function that uses two print statements to display the text below:
        hello
        world
    """
    print("hello\nworld")


def dollars_to_pounds():
    """
    Write a function called dollars_to_pounds which converts an amount in dollars
    entered by the user to a corresponding amount in pounds.
    
    Assume that the exchange rate is 1.35 dollars to the pound.
    """
    amount_of_dollars = float(input("Please enter amount of dollars to convert to pounds:"))
    print(f"{amount_of_dollars}$ = £{amount_of_dollars/1.35:.2f}")


def sum_and_difference():
    """
    Write a sum_and_difference function that asks the user to enter two numbers
    (using two separate questions)
    
    and outputs their sum and their difference (the first number minus the second number).
    """
    number_1 = int(input("Enter number 1:"))
    number_2 = int(input("Enter number 2:"))

    print(f"Sum: {number_1 + number_2}")
    print(f"Difference: {number_1 - number_2}")


def change_counter():
    """
    Write a change_counter function.
    
    This should ask the user how many 1p, 2p and 5p coins they have
    and then display the total amount of money in pence. 
    """
    one_pence_amount = int(input("Enter amount of 1p coins:"))
    two_pence_amount = int(input("Enter amount of 2p coins:"))
    five_pence_amount = int(input("Enter amount of 5p coins:"))

    print(
        f"Total amount: {one_pence_amount + two_pence_amount * 2 + five_pence_amount * 5}"
    )


def ten_hellos():
    """
    Write a ten_hellos function that uses a loop to display
        "Hello World"
    ten times (on separate lines). 
    """
    for _ in range(10):
        print("Hello World!")


def ten_hellos_mod():
    """
    Write a ten_hellos function that uses a loop to display
        "Hello World"
    ten times (on separate lines). 
    """
    print("Hello World!\n"*10)


def zoom_zoom():
    """
    Write a zoom_zoom function that asks the user for a number and outputs "zoom"
    labelled from 1 to that number
    """
    zoom_count = int(input("Enter count of zoom:"))
    for i in range(1,zoom_count+1):
        print(f"zoom {i}")


def count_to():
    """
    Write a count_to function that asks the user for a number and then counts from 1 to that number. 
    """
    count_to_number = int(input("Enter number that you wish to count to:"))
    for i in range(1, count_to_number + 1):
        print(i)


def count_from_to():
    """
    Based on your solution to the previous question,
    write a function called count_from_to that asks the user for two numbers.
    
    The first number is the start of the count and the second one is where the count ends.
    """
    count_from_number = int(input("Enter number that you wish to count from:"))
    count_to_number = int(input("Enter number that you wish to count to:"))
    for i in range(count_from_number, count_to_number + 1):
        print(i)


def weights_table():
    """
    [harder] Write a function weights_table that prints a table of kilogram weights
    (with values 10, 20, 30, …, 100) and their ounce equivalents.
    """
    for weight in range(10, 101, 10):
        print(f"{weight:4}kg | {35.274 * weight:7.2f} ounce")


def future_value():
    """
    Write a future_value function that uses a for loop to calculate the future value
    of an investment amount, assuming an annual interest rate of 3.5%.
    
    The function should ask the user for the initial amount and the number of years
    that it is to be invested, and should output the final value of the investment
    using compound interest, with the interest compounded every year

     (There is a formula to work out compound interest, but you should not use this; 
     instead, use a for loop to go through each year adding on the interest gained
     during the year.)
    """
    initial_amout = float(input("Initial amount of money:"))
    number_of_years = int(input("Please enter amount of years of prediction:"))

    predicted_amount = initial_amout
    for _ in range(number_of_years):
        predicted_amount += predicted_amount*0.035
    print(f"Predicted amount of investment after {number_of_years} years: {predicted_amount:.2f}")
