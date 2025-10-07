from dragon import Dragon
from random import randrange
class FlyingDragon(Dragon):
    def __init__(self, name, hp):
        self._swoops = 10
        super().__init__(name=name, max_hp=hp)
        
    
    def special_attack(self, hero):
        # ? Has any fire shots left?
        if self._swoops > 0:
            random_damage = randrange(5,9)
            hero.take_damage(random_damage)
            self._swoops -= 1
            return f"{self._name} just delt {random_damage} with its special attack to the hero"
            
        else:
            return f"{self._name} just delt zero damage because its out of swoops"
        
    def __str__(self):
        return f"{super().__str__()}\n   - Swoops Left: {self._swoops}"