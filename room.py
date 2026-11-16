class Room:
    def __init__(self, name: str, description: str, enemy, reward=None):
        self._name = name
        self._description = description
        self._enemy = enemy
        self._reward = reward

    def enter(self):
        print("\n" + "=" * 40)
        print(self._name)
        print(self._description)
        print("=" * 40)

        print(
            f"A {self._enemy.get_name()} appears!"
        )

    def get_enemy(self):
        return self._enemy

    def get_reward(self):
        return self._reward

    def is_cleared(self):
        return not self._enemy.is_alive()
