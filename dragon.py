from entity import Entity
from random import randrange

class Dragon(Entity):
    """Generic dragon with basic and special attacks."""

    def basic_attack(self, hero:Entity):
        """Tail attack: deal 2-5 damage and return attack."""
        damage = randrange(2,6)
        hero.take_damage(damage)
        return f"{self.name} smashes you with its tail for {damage} damage!"
    
    def special_attack(self, hero):
        """Claw attack: deal 3-7 damage and return attack."""
        damage = randrange(3,8)
        hero.take_damage(damage)
        return f"{self.name} slashes you with its claws for {damage} damage!"