class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        self.__max_health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_max_health(self):
        return self.__max_health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)

    def heal(self, amount):
        self.__health = min(
            self.__max_health,
            self.__health + amount
        )

    def is_alive(self):
        return self.__health > 0
