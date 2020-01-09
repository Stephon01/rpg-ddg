# Option lists
directions = ['north', 'south', 'east', 'west']
options = ['move', 'inventory', 'quit']
inv = ['iron sword', 'revenant armour', 'wooden roundshield', 'health potion']
import sys
# Main Menu screen
def menu():
    while True:
        print("\nMain Menu:\n")
        action = ""
        action = input("Choose an action: move, inventory quit: ")
        # Movement screen
        if action == "quit":
            sys.exit()
        elif action == 'move':
            for move in directions:
                print(move)
            move_input = input("Which direction do you want to go?")
            if move_input == "north":
                print("Going North!")
                menu()
            elif move_input == "south":
                print("Going South!")
                menu()
            elif move_input == "east":
                print("Going east!")
                menu()
            elif move_input == "west":
                print("Going west!")
                menu()
            elif move_input == "back":
                print("going back")
                menu()
            else:
                print("Invalid input")
                menu()
    # inventory screen

        elif action == "inventory":
            for inventory in inv:
                print(inventory)
            inventory_input = input("what item would you like to equip?")
            if inventory_input == "iron sword":
                print("equipiing iron sword!")
                menu()
            elif inventory_input == "health potion":
                print("using health potion!")
                menu()
            elif inventory_input == "wooden roundshield":
                print("using wooden roundshield")
                menu()
            elif inventory_input == "revenant armour":
                print("equiping revenant armour")
                menu()
            else:
                print("Invalid input")
                menu()
        else:
            print("Invalid input")
            menu()
# menu call
menu()
