
from hero import Hero
from dragon import Dragon
from fly import FlyingDragon
from fire import FireDragon
from check_input import get_int_range
from random import randrange
def main():
    hero_name = input("What is your name, challenger?\n")
    hero = Hero(name=hero_name, max_hp=50)
    list_of_dragons = [Dragon(name="Smaug",max_hp=20), FireDragon(name="Toothless", hp=20), FlyingDragon(name="Drogon",hp=20)]
    print(f"Welcome to dragon training {hero._name}\nYou must defeat {list_of_dragons.__len__()} dragons\n\n")
    # main loop
    user_won = False
    while True:
        # remove any dragon that is dead
        list_of_dragons = [d for d in list_of_dragons if d._hp > 0]

        print(hero.__str__())
        index = 1
        for dragon in list_of_dragons:
            print(str(index)+". Attack " + dragon.__str__())
            index += 1
        dragon_to_attack_index =  get_int_range("Choose a dragon to attack: ",1,index) -1
        print("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")        
        weapon_selection =  get_int_range("Enter weapon: ",1,2)
        
        if weapon_selection == 1:
            print(hero.arrow_attack(list_of_dragons[dragon_to_attack_index]))
            
        elif weapon_selection == 2:
            print(hero.sword_attack(list_of_dragons[dragon_to_attack_index]))

        # Clear any dragons that may have died before allowing them to attack
        list_of_dragons = [d for d in list_of_dragons if d._hp > 0]

             

        # ! This should randomly select a live dragon, this is because im lazy and will fix later that it iteratively goes in order
        if len(list_of_dragons) == 0:
            user_won = True
            break
            
        random_dragon_index = randrange(1,len(list_of_dragons)+1)-1
        
        random_attack_decider = randrange(0,11)
        if random_attack_decider % 2 == 0:
            print(list_of_dragons[random_dragon_index].basic_attack(hero=hero))
        else:
            print(list_of_dragons[random_dragon_index].special_attack(hero=hero))
        
        if hero._hp <= 0:
            break

    if user_won:
        print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
    else:
        print("You died")


if __name__ == "__main__":
    main()