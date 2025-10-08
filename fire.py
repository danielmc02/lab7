from dragon import Dragon
from random import randrange
from entity import Entity

class FireDragon(Dragon):
    """Dragon that breathes fire a limited number of times."""

    def __init__(self, name, hp):
        """Create a FireDragon and set the number of fire shots."""
        self._fire_shots = 2
        super().__init__(name=name, max_hp=hp)

    def special_attack(self, hero:Entity):
        """Fire breath: 6-9 damage if shots remain; otherwise no damage."""
        if self._fire_shots > 0:
            dmg = randrange(6,10)
            hero.take_damage(dmg)
            self._fire_shots -= 1
            return f"{self.name} engulfs you in flames for {dmg} damage!"
            
        else:
            return f"{self.name} tries to spit fire at you but is all out of fire shots."
        
    def __str__(self):
        """Displays number of remaining fire shots."""
        return f"{super().__str__()}\nFire Shots remaining: {self._fire_shots}"