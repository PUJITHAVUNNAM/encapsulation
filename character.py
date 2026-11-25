class Character:
    def __init__(self, health, max_health):
        self.__health = health
        self.__max_health = max_health

    @property
    def health(self):
        return self.__health

    def damage(self, points):
        self.__health = max(0, self.__health - points)

    def heal(self, points):
        self.__health = min(self.__max_health, self.__health + points)


c = Character(80, 100)

print("Current Health:", c.health)

c.damage(30)
print("After Damage:", c.health)

c.heal(40)
print("After Healing:", c.health)

c.heal(50)
print("Final Health:", c.health)