
# Course: CS 30
# Period: 1
# Date created: 19/10/08
# Date last modified: 19/11/15
# Name: Stephon Murray
# Description: Nested Dictionary


#Dictionary for Weapons
Weapons = {
  "Weapon1" : {
    "Weapon name" : "Revenant Sword",
    "Damage" : "18Dps(DamagePerSecond)"
  },
  "Weapon2" : {
    "Weapon name" : "Z1 Spear",
    "Damage" : "12Dps(DamagePerSecond)"
  },
  "Weapon3" : {
    "Weapon name" : "Basic Dagger",
    "Damage" : "6Dps(DamagePerSecond)"
  }
}



#Dictionary for Armour
Armour_peace = {
    "Armour name" : "Basic Helmet",
    "Health Points" : "10(HealthPoints)"
}


#Dictionary for Armour
Armour_piece = {
    "Armour name" : "Revenant Helmet",
    "Health Points" : "30Hp(HaalthPoints)"
}

#Loops and print statements
for item in Weapons:
    print(item)
    for x in Weapons[item]:
        weapon =  Weapons[item][x]
        print(f"{weapon}\n")


for armour in Armour_peace:
    print(armour)
    b = Armour_peace[armour]
    print(f"{b}\n")


for armour1 in Armour_piece:
    print(armour1)
    y = Armour_piece[armour1]
    print(f"{y}\n")
