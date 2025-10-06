from entity import Entity
from random import randrange
class Hero(Entity):
    def sword_attack(self, dragon:Entity):
        # Rolls two 6-sided dice
        dice_one = randrange(1,7)
        dice_two = randrange(1,7)
        total_damage = dice_one+dice_two
        dragon.take_damage(total_damage)
        return f"You hit the dragon with {total_damage} damage points from your sword"
    
    def arrow_attack(self, dragon:Entity):
        # Rolls one 12-sided dice
        dice_one = randrange(1,13)
        dragon.take_damage(dice_one)
        return f"You hit the dragon with {dice_one} damage points from your arrow"