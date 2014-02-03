#Copywrite (c) Paul Ashby 2014
#Weight Effect
#First Game

print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\\ \\ \\ \\ Weight Effect \\ \\ \\ \\")
print("\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\nBy Paul Ashby")

main = input("\n\nWelcome, would you like to start a new game or exit?\n(new or exit)\n:>")

#------Imported Modules------#
import random
#------Defined Variables------#
wave = 1
#------Defined Lists------#
dwarf = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

#------Defined Functions------#
def char_Inventory():
        print("Here is what your character looks like so far."
              "\nName:", dwarf[0],
              "\nStrength:", dwarf[1],
              "\nDexterity:", dwarf[2],
              "\nInteligence:", dwarf[3],
              "\nDamage:", dwarf[4],
              "\nArmor:", dwarf[5],
              "\nPotions:", dwarf[6],
              "\nHP:", dwarf[7],
              "\nGold:", dwarf[8])

def character_creation():
        print("Character Creation.")
        newdwarf = []
        newdwarf.append(input("Enter a name for your dwarf.\n:>"))
        print("Your dwarf is named", newdwarf[0], ".")
        print("\nTime to roll your stats!")
        input("Press enter to roll for your strength.")
        newdwarf.append(random.randint(1, 20)) #Str
        print("You rolled a", newdwarf[1], "for your strength.")
        input("Press enter to roll for your dexterity.")
        newdwarf.append(random.randint(1, 20)) #Dex
        print("You rolled a", newdwarf[2], "for your dexterity.")
        input("Press enter to roll for your intelligence.")
        newdwarf.append(random.randint(1, 20)) #Int
        print("You rolled a", newdwarf[3], "for your inteligence.")
        input("Press enter to roll for your starting axe damage.")
        newdwarf.append(random.randint(1, 20)) #Damage
        print("Your initial axe damage is", newdwarf[4],".")
        input("Press enter to roll for your initial armor value.")
        newdwarf.append(random.randint(1, 18)) #Armor
        print("Your inital armor will resist", newdwarf[5], "points of damage.")
        newdwarf.append(random.randint(0, 0)) #Potions
        print("You will start out with 0 potions.")
        input("Press enter to see your health (HP).")
        newdwarf.append(100 + newdwarf[1])
        print("Your initial HP is 100 plus your strength which comes to", newdwarf[7], "HP.")
        input("Press enter to see your starting wealth.")
        newdwarf.append(random.randint(50, 100))
        print("Your initial wealth is", newdwarf[8], "gold.")
        return newdwarf

def stat_modder(x, y, z, a):
#x is the stat list, y is the stat location,
#z is the new value, a is the command flag
    stat = x

    if (a == 1):#A 1 value for A mean generate character stats
        for i in range(1, 4):
            stat[i] = random.randint(1,20)
        stat[5] = random.randint(1, 18)
        stat[7] = 100 + stat[1]
        stat[8] = random.randint(50, 100)

    elif(a == 2):#A 2 value for A means generate magic stats
        for i in range(3):
            stat[i] = random.randint(1, 20)
        stat[3] = 1
        stat[4] = 1

    elif(a == 3):#A 3 value for A mean modify a stat
        stat[y] = z
    else:
        print('Burn the heretic')
    return stat

def shopCommands():
        print("List of commands:",
              "\nlist : Shows list of commands.",
              "\nshopinv : Prints shop inventory.",
              "\ninv : Prints your inventory,",
              "\nbuy : Asks to buy an item from the shop.",
              "\nexit : Exits the shop.")

def shop():
        storeInventory = []
        storeInventory.append(random.randint(1, 20) * wave) #Weapons
        storeInventory.append(random.randint(1, 18) * wave) #Armor
        storeInventory.append(random.randint(1, 6) * wave) #Potions
        print("WELCOME TO YE OLD LOCAL SHOPPE")
        print("Our current inventory consists of the following items:")
        print("An axe that can do", storeInventory[0], "damage.")
        print("A set of armor that protects against", storeInventory[1], "points of damage.")
        print("We also have", storeInventory[2], "health potion(s).")
        shopCommands()
        sCommand = input("Please enter a command from the list.")
        while sCommand != "exit":
                sCommand = input("Please enter a command from the list.")
                if sCommand == "list":
                        shopCommands()
                elif sCommand == "shopinv":
                        print("Our current inventory consists of the following items:")
                        print("An axe that can do", storeInventory[0], "damage.")
                        print("A set of armor that protects against", storeInventory[1], "points of damage.")
                        print("We also have", storeInventory[2], "health potion(s).")
                elif sCommand == "inv":
                        print("You have the following in your inventory.",
                              "\nAn axe that can do", dwarf[4], "damage.",
                              "\nA set of armor that can withstand", dwarf[5], "points of damage.\n",
                              dwarf[6], "Health potions.\n",
                              dwarf[8], "Gold.")
                elif sCommand == "buy":
                        print("You can buy the following items:")
                        print("(1) = Axe",
                              "(2) = Armor",
                              "(3) = Potions")
                        purchase = input("Buy an item from the shop by entering the number that coorosponds to that item.")
                        if purchase == "1": #buying the axe.
                                cost = storeInventory[0] * wave
                                print("This axe will cost", cost, "gold.")
                                purchase = input("Do you still want to buy this axe?\n(y/n)\n:>")
                                if purchase == "y":
                                        posEight = int(dwarf[8])
                                        if posEight < cost:
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                break
                                        else:
                                            del dwarf[4]
                                            dwarf.insert(4, storeInvetory[0])
                                            posEight -= cost
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        charInventory()
                                else:
                                    break
                        elif purchase == "2": #buying the armor.
                                cost = storeInventory[1] * wave
                                print("This armor will cost", cost, "gold.")
                                purchase = input("Do you still want to buy this armor?\n(y/n)\n:>")
                                if purchase == "y":
                                        posEight = int(dwarf[8])
                                        if posEight < cost:
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                break
                                        else:
                                            del dwarf[5]
                                            dwarf.insert(5, storeInvetory[1])
                                            posEight -= cost
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        charInventory()
                                else:
                                    break
                        elif purchase == "3": #buying some potions.
                                cost = storeInventory[2] * wave
                                print("Each potion will cost", cost, "gold.")
                                purchase = input("Do you still want to buy some potions?\n(y/n)\n:>")
                                if purchase == "y":
                                        numberPotions = int(input("How many potions do you want to buy?\n:>"))
                                        if numberPotions > storeInventory[3]:
                                                print("THERE ARE NOT THAT MANY POTIONS IN THE STORE!")
                                                break
                                        posEight = int(dwarf[8])
                                        if posEight < (cost * numberPotions):
                                                print("YOU DON'T HAVE THAT KIND OF MONEY!")
                                                break
                                        else:
                                            del dwarf[6]
                                            dwarf.insert(6, numberPotions)
                                            posEight -= (cost * numberPotions)
                                            del dwarf[8]
                                            dwarf.insert(8, posEight)
                                        charInventory()
                                else:
                                    break


#------MAIN LOOP------#
while main == "new":
    for i in range(5): #This loop controls character creation.
        character_creation()
        reroll = input("Do you want to reroll your character? (y/n)\n:>")
        if reroll == "n":
            break
        else:
            print("You can reroll your dwarf", 5 - (i + 1), "more times.")
        dwarf = [character_creation()]
        charInventory()
    spend = input("Do you want to go to a shop before you fight endless waves of monsters?\n(y/n)\n:>")
    if spend == "y":
            shop()
    
    break
