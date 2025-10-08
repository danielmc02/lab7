from dragon import Dragon
from random import randrange
from entity import Entity

class FlyingDragon(Dragon):
    """Dragon that can swoop a limited number of times."""

    def __init__(self, name, hp):
        """Create a FlyingDragon and set the number of swoops."""
        self._swoops = 3
        super().__init__(name=name, max_hp=hp)
        
    def special_attack(self, hero):
        """Swoop: 5-8 damage if swoops remain; otherwise no damage."""
        if self._swoops > 0:
            dmg = randrange(5,9)
            hero.take_damage(dmg)
            self._swoops -= 1
            return f"{self.name} swoops down and hits you for {dmg} damage!"
            
        else:
            return f"{self.name} tries to swoop, but is out of swoops."
        
    def __str__(self):
        """Displays number of remaining swoops."""
        return f"{super().__str__()}\nSwoop attacks remaining: {self._swoops}"