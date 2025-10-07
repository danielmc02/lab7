
from entity import Entity
from random import randrange


class Dragon(Entity):
    def basic_attack(self, hero:Entity):
        #takes a random amount of damage in the range 2-5
        damage = randrange(2,6)
        hero.take_damage(damage)
        return f"{self._name} used it's basic attack, damaging the hero by {damage} points"
    
    def special_attack(self, hero):
        damage = randrange(3,8)
        hero.take_damage(damage)
        return f"{self._name} used it's special attack, damaging the hero by {damage} points"