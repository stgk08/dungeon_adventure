class character:
    def __init__(self, name:str, health):
        self.__name = navn
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


    
