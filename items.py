class Weapon:
    def __init__(item):
        raise NotImplementedError("Do not create raw Weapon objects.")

        def __str__(item):
            return item.name

class Z1Spear(Weapon):
    def __init__(item):
     item.name = "Z1Spear"
item.description = "A high level Spear, suitable for combat"
item.damage = 20
