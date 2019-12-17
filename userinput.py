# Option lists
directions = ['north', 'south', 'east', 'west']
options = ['move', 'inventory']
inv = ['iron sword', 'bronze chestplate', 'wooden roundshield', 'health potion']


# Main Menu screen
def menu():
    print("\nMain Menu:\n")
    for option in options:
        print(f"\t{option.title()}\n")
    response = ""

    response = input("What would you like to do?\n")
    if response == 'move':
        move()
    elif response == 'inventory':
        inventory()
    else:
        print("I didn't understand that\n")


# Movement Menu screen
def move():
    print("\nMovement Directions:\n")
    for direction in directions:
        print(f"\t{direction.title()}\n")
    response = ""
    response = input("Type 'north/south/east/west' or 'back' to access the main menu\n")
    if response == 'north':
        print("You head north")
        menu()
    elif response == 'south':
        print("You head south")
        menu()
    elif response == 'east':
        print("You head east")
        menu()
    elif response == 'west':
        print("You head west")
        menu()
    elif response == 'back':
        menu()
    elif response == 'd':
        print("deez nuts")
    else:
        print("I didn't understand that\n")


# Inventory screen
def inventory():
    print("\nInventory:\n")
    for item in inv:
        print(f"\t{item.title()}\n")
    response = ""
    response = input("Type 'back' to access the main menu\n")
    if response == 'back':
        menu()
    else:
        print("I didn't understand that\n")


# Main Menu function call
menu()
