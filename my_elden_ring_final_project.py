"""  
ask the user for a new elden ring weapon
they will give this weapon stats 
if they give a lot to strength they won't have much for other categories
The code will print out what other weapons are better or worse, or which bosses are weak or strong against it
if user mentions the weapon is a sword, hammer, axe, scyth, bow, etc. it'll draw it on canvas

"""


SOME_WEAPONS = {"Godslayer's Greatsword": {"Phys": 119, "Mag": 0, "Fire": 77, "Ligt": 0, "Holy": 0, "Crit": 100, "Wgt.": 17.5},
                "Sword of Night and Flame": {"Phys": 87, "Mag": 56, "Fire": 56, "Ligt": 0, "Holy": 0, "Crit": 100, "Wgt.": 4.0},
                "Grave Scythe": {"Phys": 144, "Mag": 0, "Fire": 0, "Ligt": 0, "Holy": 0, "Crit": 100, "Wgt.": 9.5},
                "Greatsword of Damnation": {"Phys": 123, "Mag": 0, "Fire": 0, "Ligt": 0, "Holy": 79, "Crit": 100, "Wgt.": 8.0},
                "Marais Executioner's Sword": {"Phys": 123, "Mag": 0, "Fire": 0, "Ligt": 0, "Holy": 79, "Crit": 100, "Wgt.": 8.0},
                "Bolt of Gransax": {"Phys": 98, "Mag": 0, "Fire": 0, "Ligt": 63, "Holy": 0, "Crit": 100, "Wgt.": 8.5},
                "Blasphemous Blade": {"Phys": 121, "Mag": 0, "Fire": 78, "Ligt": 0, "Holy": 79, "Crit": 100, "Wgt.": 13.5},
                "Wing of Astel": {"Phys": 65, "Mag": 78, "Fire": 0, "Ligt": 0, "Holy": 0, "Crit": 100, "Wgt.": 2.5},
                "Rivers of Blood": {"Phys": 76, "Mag": 0, "Fire": 76, "Ligt": 0, "Holy": 0, "Crit": 100, "Wgt.": 6.5},
                "Golden Epitaph": {"Phys": 85, "Mag": 0, "Fire": 0, "Ligt": 0, "Holy": 85, "Crit": 100, "Wgt.": 3.5},
                "Cipher Pata": {"Phys": 0, "Mag": 78, "Fire": 0, "Ligt": 0, "Holy": 85, "Crit": 100, "Wgt.": 0.0},
                "Zweihander": {"Phys": 141, "Mag": 0, "Fire": 0, "Ligt": 0, "Holy": 0, "Crit": 100, "Wgt.": 15.5}
                }
            

def main():
  
    user_weapon = get_user_weapon() #is a dict. type variable
    user_weapon_name = user_weapon.pop("Name") #now the format of the weapon_name dict. matches the weapons in SOME_WEAPONS
    compare_weapons(user_weapon, user_weapon_name)
    

def compare_weapons(user_weapon, user_weapon_name):
    print('')
    lst_weapon_names = []
    for weapon in SOME_WEAPONS.keys(): #could just use .keys(), but whatever .items() works too
        lst_weapon_names.append(weapon)

    print(f"Which weapon do you want to compare {user_weapon_name} to? Your options are:\n\n" + ", ".join(weapon for weapon in lst_weapon_names))
    comparison_weapon = input("Input a weapon from the list: ")
    while comparison_weapon not in lst_weapon_names:
        comparison_weapon = input("That is not a weapon in the list, try again: ")
    print("\nLet's compare...\n")
    
    lst_attributes = list(user_weapon.keys())
    lst_user_weapon_stats = list(user_weapon.values())
    lst_comparison_weapon_stats = list(SOME_WEAPONS[comparison_weapon].values())
    print(f"      {user_weapon_name:^37} {comparison_weapon:^37}")
    for i in range(7):
        if lst_user_weapon_stats[i] < lst_comparison_weapon_stats[i]:
            comparison = "<"
        elif lst_user_weapon_stats[i] > lst_comparison_weapon_stats[i]:
            comparison = ">"
        else:
            comparison = "="
        
        print(f"{lst_attributes[i]:<4}: {lst_user_weapon_stats[i]:<37}{comparison}{float(lst_comparison_weapon_stats[i]):>37} ")



def get_user_weapon(): #will return user_weapon as a dictionary type variabl
    user_weapon = {} # haven't implemented anything to force the user to put a reasonable number (not text, not too high or low)
    name = input("Greetings tarnished. What do you name your mighty weapon? ")
    user_weapon = {'Name':name}
    print('')

    get_stat(user_weapon, "Phys", 165) #third number represents the max that a user may input for this stat
    get_stat(user_weapon, "Mag", 80)
    get_stat(user_weapon, "Fire", 80)
    get_stat(user_weapon, "Ligt", 80)
    get_stat(user_weapon, "Holy", 80)
    get_stat(user_weapon, "Crit", 140)
    get_stat(user_weapon, "Wgt.", 26.5)

    return user_weapon
    

def get_stat(user_weapon, attribute, max_range): 
#the dictionary user_weapon is passed by reference, so changes made to it in the local function affect the dictionary outside of the local function too because it is mutable
#whereas when you pass by value, changes made in the local function don't affect the variable outside of it
    while True:
        chosen_stat = input(f"Enter your weapon's {attribute} stat: ")
        try: #makes sure they didn't enter words
            chosen_stat = float(chosen_stat)
        except ValueError:
            print("Please enter numbers only")
        else:
            if (0<= chosen_stat <= max_range):
                break
            elif (chosen_stat > max_range):
                print(f"The {attribute} stat cannot go that high")
            else:
                print(f"The {attribute} stat cannot be negative")

    user_weapon[attribute] = chosen_stat

if __name__ == "__main__":
    main()