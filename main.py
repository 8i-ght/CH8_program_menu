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

#2nd Program:
def sum_of_digits():
menu_navigation()