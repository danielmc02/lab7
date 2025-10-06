
from hero import Hero
from dragon import Dragon
from fly import FlyingDragon
from fire import FireDragon
from check_input import get_int_range
from random import randrange
def main():
    hero_name = input("What is your name, challenger? \n")
    hero = Hero(name=hero_name, max_hp=100)
    list_of_dragons = [Dragon(name="Smaug",max_hp=120),FlyingDragon(name="Toothless", hp=120), FlyingDragon(name="Drogon",hp=110)]
    print(f"Welcome to dragon training {hero._name}\nYou must defeat {list_of_dragons.__len__()} dragons\n\n")
    # main loop
    while True:
        print("/n"+hero.__str__() + "\n")
        index = 1
        for dragon in list_of_dragons:
            print(str(index)+". " + dragon.__str__())
            index += 1
        dragon_to_attack_index =  get_int_range("Choose a dragon to attack: ",1,3) -1
        print("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")        
        weapon_selection =  get_int_range("Enter weapon: ",1,2)
        
        if weapon_selection == 1:
            print(hero.arrow_attack(list_of_dragons[dragon_to_attack_index]))
            
        elif weapon_selection == 2:
            print(hero.sword_attack(list_of_dragons[dragon_to_attack_index]))

        # choose a random (surviving) dragon that will attack the user, and randomly choose
        # either a basic or special attack and display the attack message 
        random_dragon_still_alive: Dragon

        # ! This should randomly select a live dragon, this is because im lazy and will fix later
        for dragon in list_of_dragons:
            if dragon._hp > 0:
                random_dragon_still_alive = dragon
        random_attack_decider = randrange(0,11)
        if random_attack_decider % 2 == 0:
            print(random_dragon_still_alive.basic_attack(hero=hero))
        else:
            print(random_dragon_still_alive.special_attack(hero=hero))

        


if __name__ == "__main__":
    main()