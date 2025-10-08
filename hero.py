from entity import Entity
from random import randrange

class Hero(Entity):
    """Player-controlled hero with two attack options."""

    def sword_attack(self, dragon:Entity):
        """Sword: roll 2D6 damage and return attack."""
        d1 = randrange(1,7)
        d2 = randrange(1,7)
        total = d1 + d2
        dragon.take_damage(total)
        return f"You slash the {dragon.name} with your sword for {total} damage."
    
    def arrow_attack(self, dragon:Entity):
        """Arrow: roll 1D12 damage and return attack."""
        dmg = randrange(1,13)
        dragon.take_damage(dmg)
        return f"You hit the {dragon.name} with an arrow for {dmg} damage."