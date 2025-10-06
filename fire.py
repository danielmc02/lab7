from dragon import Dragon
from random import randrange
from entity import Entity

class FireDragon(Dragon):
    def __init__(self, name, hp):
        self._fire_shots = 10
        super().__init__(name=name, max_hp=hp)

    def special_attack(self, hero:Entity):
        # ? Has any fire shots left?
        if self._fire_shots > 0:
            random_damage = randrange(6,10)
            hero.take_damage(random_damage)
            self._fire_shots -= 1
            return f"Fire dragon just delt {random_damage} with its special attack"
            
        else:
            return f"Fire dragon delt zero damage because its out of fire shots"
        
    def __str__(self):
        return f"{super().__str__()}\n  Fire Shots Left: {self._fire_shots}"