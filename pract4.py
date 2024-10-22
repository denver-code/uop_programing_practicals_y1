def personal_greeting():
    print(f"Hello {input('Please enter your name:')}, nice to see you!")


def formal_name():
    print(f"{input('Please enter your given name:')[0]}. {input('Please enter your family name:')}")


def generate_email():
    surname = input("Please enter your surname:")
    forename = input("Please enter your forename:")
    entry_year = input("What year did you entered university [two digits]:")

    email = f"{surname[:5]}.{forename[0]}.{entry_year}@myport.ac.uk"
    print(email)


def name_to_number():
    name = input("Please enter your name:").lower()

    name_value = 0 
    for ch in name: 
        name_value += ord(ch) - 96

    print(name_value)    


def rainfall_chart():
    with open("text_files/rainfall.txt", "r") as file:
        data = file.readlines()

    for chart in data:
        chart = chart.replace("\n", "").split()
        print(f"{chart[0]} {'*' * int(chart[1])}")
        

def rainfall_in_inches():
    with open("text_files/rainfall.txt", "r") as file:
        data = [i.replace("\n", "").split() for i in file.readlines()]

    with  open("text_files/rainfallInches.txt", "w") as file:
        file.write("\n".join(
            " ".join(
                [city, f"{int(chart) /  25.4:.2f}"]) for city, chart in data
            )
        )


def wc():
    filename = input("Please enter filename:")

    with open(filename, "r") as file:
        data = file.read()
        char_amount = len(data)
        words_amount = len(data.split())
        lines_amount = len(data.split("\n"))
    
    print(f"Characters: {char_amount} Words: {words_amount} Lines: {lines_amount}")

wc()