
class Room:
    def __init__(self, name, description, enemy, reward=None):
        self.__name = name
        self.__description = description
        self.__enemy = enemy
        self.__reward = reward

    def enter(self):
        print("\n" + "=" * 40)
        print(self.__name)
        print(self.__description)
        print("=" * 40)

        print(
            f"A {self.__enemy.get_name()} appears!"
        )

    def get_enemy(self):
        return self.__enemy

    def get_reward(self):
        return self.__reward

    def is_cleared(self):
        return not self.__enemy.is_alive()
