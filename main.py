import calendar
# This homework assignment is a series of programs that perform different tasks
# 1: This program gets a string containing a persons's first, middle and last names, and displays their first middle, and last initials
# 2: This program asks the user to enter a series of single digit numbers with nothing separating them.
# The program will display the sum of all the single digit numbers in the string. Ex. user enters: 2514, program returns: 12
# 3: This program converts a date that is entered in the following format mm/dd/yyyy to the following format: month day, year
# 4: This program asks the user to enter a sentence and then converts the sentence to pig latin. (In Pig Latin you remove the first letter and place it at the end of the word then append "ay" to the end of the string)

# This will be a menu that I create to allow the user to select which program they want to run
def menu():
    print("Please select a program to run")
    print("1: Get initials")
    print("2: Sum of digits")
    print("3: Convert date")
    print("4: Convert to pig latin")
    print("5: Exit")
    # Validate user's choice to make sure only int's between 1-5 are chosen
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid choice, please try again")

# Function for navigation through the menus
def menu_navigation():
    choice = menu()
    if choice == 1:
        get_initials()
    elif choice == 2:
        sum_of_digits()
    elif choice == 3:
        convert_date()
    elif choice == 4:
        convert_to_pig_latin()
    elif choice == 5:
        print("Exiting Program . . .")

# 1st Program:
def get_initials():
    # Get the users full name
    first_name = input("Enter the users first name: ")
    middle_name = input("Enter the users middle name: ")
    last_name = input("Enter the users last name: ")
    # Print out the users initials
    print(f"The users initials are {first_name[0].upper()}. {middle_name[0].upper()}. {last_name[0].upper()}.")
    # Run the program again
    menu_navigation()

# 2nd Program:
def sum_of_digits():
    while True:
        # Try and expect to make sure user only enters integers
        try:
            # Get user to input numbers
            user_digit_input = input("Enter the numbers you want to see the sum of: ")
            # Create a list that loops through the string and turns all of the characters into integers
            user_digits_array = [int(digit) for digit in user_digit_input]
            # Add them up and print it out
            user_digits_sum = sum(user_digits_array)
            print(f'The sum of the digits is: {user_digits_sum}')
            menu_navigation()
        except ValueError:
            print("Please only enter integers")

# 3rd Program
def convert_date():
    # Prompt user to enter the date
    user_input_date = input("Enter a date in the form mm/dd/yyyy: ")
    # Split into an array of strings
    date_components = user_input_date.split("/")
    # Check if import has three components
    if len(date_components) != 3:
            print("Please enter the date in the correct format")
            convert_date()
    # Assign variables for the different parts of the array
    month, day, year = date_components
    # Check to make sure the variables contain only ints
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        print("Please use only integers")
        convert_date()
    # Convert the variables to ints
    month = int(month)
    day = int(day)
    year = int(year)
    # Validate the length of the month, day, and year
    if not(1 <= month <= 12):
        print("The date must be between 1 and 12")
        convert_date()
    if not(1 <= day <= 31):
        print("The date must be between 1 and 31")
        convert_date()
    if year < 0:
        print("The year must be a positive number")
        convert_date()
    # Convert the month number to the name of the month
    month_name = calendar.month_name[month]
    # Print out the final result
    print(f"The date you entered was {month_name}, {day}, {year}")
    menu_navigation()

# 4th Program
def convert_to_pig_latin():
    # Prompt the user to input their sentence
    piglatin_user_input = input("Enter the string you wish to be converted to pig latin: ")
    # Check that the user entered something
    if not piglatin_user_input.split():
        print("Please enter something")
        convert_to_pig_latin()
    # Convert the string to an array 
    piglatin_array = piglatin_user_input.split()
    # Create array to store the result in
    piglatin_result = []
    # Loop through each word in the array and convert them to piglatin
    for word in piglatin_array:
            piglatin_transfer = word[1:] + word[0] + "ay"
            piglatin_result.append(piglatin_transfer)
    # Convert the array of strings to a single string
    piglatin_sentence = " ".join(piglatin_result)
    # Show the user their result
    print(f"Your sentence in pig latin is: {piglatin_sentence}")
    menu_navigation()
menu_navigation()