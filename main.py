"""
LAB #7
    10/08/2025
    Student 1: Jimmy Le
    Student 2: Daniel McCray

    Dragon Trainer: Construct a Hero and three dragons (Dragon, FireDragon, FlyingDragon).
      Each round: player chooses a dragon and an attack (sword/arrow), damage is applied, defeated dragons are removed.
      Then a random living dragon counterattacks (basic/special). Game ends when all dragons are defeated or the hero reaches 0 HP.
      All input is validated.
"""
from hero import Hero
from dragon import Dragon
from flying import FlyingDragon
from fire import FireDragon
from check_input import get_int_range
from random import randrange

def main():
    """Run the Dragon Trainer until all dragons are dead or Hero loses HP."""
    hero_name = input("What is your name, challenger?\n")
    hero = Hero(name=hero_name, max_hp=50)

    list_of_dragons = [
        Dragon(name="Deadly Nadder", max_hp=10),
        FireDragon(name="Gronckle", hp=15),
        FlyingDragon(name="Timberjack", hp=20),
        ]
    
    print(f"Welcome to dragon training, {hero.name}\nYou must defeat {len(list_of_dragons)} dragons.\n")

    # main loop
    user_won = False
    while True:
        # remove any dragon that is dead
        list_of_dragons = [d for d in list_of_dragons if d.hp > 0]

        print()

        print(hero)  # e.g., Astrid: 50/50
        for i, d in enumerate(list_of_dragons, start=1):
            # d.__str__ prints "Name: hp/max" (+ extra line for Fire/Flying)
            print(f"{i}. Attack {d}")

        # choose dragon (validate 1..len)
        dragon_to_attack_index = get_int_range("Choose a dragon to attack: ", 1, len(list_of_dragons)) - 1

        # weapon menu
        print("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")
        weapon_selection = get_int_range("Enter weapon: ", 1, 2)

        # hero attacks chosen dragon
        target = list_of_dragons[dragon_to_attack_index]
        if weapon_selection == 1:
            print(hero.arrow_attack(target))
        else:
            print(hero.sword_attack(target))

        # announce defeat immediately if target hits 0 and remove it before enemy turn
        if target.hp == 0:
            print(f"You defeated the {target.name}!")
        list_of_dragons = [d for d in list_of_dragons if d.hp > 0]

        # check win
        if len(list_of_dragons) == 0:
            user_won = True
            break

        # random living dragon attacks back; randomly choose basic or special
        rand_idx = randrange(0, len(list_of_dragons))
        attacker = list_of_dragons[rand_idx]
        # pick basic/special 50/50
        if randrange(0, 2) == 0:
            print(attacker.basic_attack(hero))
        else:
            print(attacker.special_attack(hero))

        # check hero death
        if hero.hp <= 0:
            break

    if user_won:
        print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
    else:
        print("You died")

if __name__ == "__main__":
    main()