import items

class player:
    def __init__(user):
        user.inventory = [items.Z1Spear()]

    def print_inventory(user):
        print("Inventory:")
        for item in user.inventory:
            print('* ' + str(item))
        best_weapon = user.most_powerful_weapon()
        print("Your best and only weapon is your {}".format
        (best_weapon))

    def most_powerful_weapon(user):
        max_damage = 0
        best_weapon = None
        for item in user.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
