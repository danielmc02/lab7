class Entity:
    """Base for any character with name and HP."""

    def __init__(self, name, max_hp):
        """Creates an entity with name and starting/max HP."""
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    @property
    def name(self):
        """Read-only access to the entity's name."""
        return self._name

    @property
    def hp(self):
        """Read-only access to the entity's current HP."""
        return self._hp
    
    @property
    def max_hp(self):
        """Read-only access to the entity's max HP."""
        return self._max_hp

    def take_damage(self, dmg):
        """Reduce HP by dmg but never below 0."""
        if self._hp - dmg < 0:
            self._hp = 0
        else:
            self._hp -= dmg

    def __str__(self):
        """Return status in the format 'Name: hp/max_hp'."""
        return f"{self._name}: {self._hp}/{self._max_hp}"