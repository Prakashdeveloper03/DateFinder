# A python module for locating dates inside text.
# Use this package to extract all sorts of date like strings from a document and turn them into datetime objects.
# This module finds the likely datetime strings and then uses `dateutil` to convert to the datetime object.

from datefinder import find_dates  # pip install datefinder

flag = True  # Until Loop
while flag:
    # gets the user input as string value and stores it in `user_input` variable
    print(
        "\n1. Find dates from the given string\n2. Find dates from the given string with Source value\n3. Find dates from the given string with Source index\n4. Exit"
    )
    option = int(input("Enter the Option : "))
    match option:
        case 1:
            user_input = input("Enter the number : ")
            print("Found Dates : ")
            # returns a generator that produces datetime.datetime objects
            for date in find_dates(user_input):
                print(date)
        case 2:
            user_input = input("Enter the number : ")
            print("Found Dates : ")
            # Find dates also return the original string segment
            for date in find_dates(user_input, source=True):
                print(f"{date[0]} --> {date[1]}")
        case 3:
            user_input = input("Enter the number : ")
            print("Found Dates : ")
            # Find dates also return the indices where the datetime string was located in text
            for date in find_dates(user_input, index=True):
                print(f"{date[0]} --> {date[1]}")
        case 4:
            flag = False
        case _:
            print("Invalid Option\nPlease, Enter a valid option...")
