


class Entity:
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    def take_damage(self, dmg):
        if self._hp - dmg < 0:
            self._hp = 0
        else:
            self._hp -= dmg


    def __str__(self):
        return f"{self._name}: {self._hp}/{self._max_hp}"