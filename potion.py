class Potion:
    def __init__(self, healing):
        self.__healing = healing
        self.__used = False

    def use(self, player):
        if self.__used:
            print("You have already used your potion!")
            return

        if not player.is_alive():
            print("You cannot use a potion!")
            return

        player.heal(self.__healing)
        self.__used = True

        print(f"You restored {self.__healing} HP!")
