# Character
class Character:
    def __init__(self, name: str, health):
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
        self.__health = min(self.__max_health, self.__health + amount)

    def is_alive(self):
        return self.__health > 0


# Weapon
class Weapon:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage


# Potion
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


# Enemy
class Enemy(Character):
    def __init__(self, name: str, health: int, damage: int):
        super().__init__(name, health)
        self._damage = damage

    def attack(self, player):
        player.take_damage(self._damage)
        print(f"{self.get_name()} attacked you and dealt {self._damage} damage!")


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 5)


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 30, 8)


class Boss(Enemy):
    def __init__(self):
        super().__init__("Dragon", 60, 12)


# Player
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100)

        self.__weapon = Weapon("Rusty Sword", 15)
        self.__potion = Potion(40)
        self.__defending = False

    def attack(self, target):
        damage = self.__weapon.get_damage()
        target.take_damage(damage)

        print(
            f"{self.get_name()} attacks "
            f"{target.get_name()} for {damage} damage!"
        )

    def defend(self):
        self.__defending = True
        print("You are defending!")

    def take_damage(self, amount):
        if self.__defending:
            amount = amount // 2
            self.__defending = False
            print("Your defense reduced the damage!")

        super().take_damage(amount)

        print(f"You have {self.get_health()} HP left.")

    def use_potion(self):
        self.__potion.use(self)

    def equip_weapon(self, weapon):
        self.__weapon = weapon
        print(f"You equipped {weapon.get_name()}!")

    def get_weapon(self):
        return self.__weapon


# Room
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

        print(f"A {self._enemy.get_name()} appears!")

    def get_enemy(self):
        return self._enemy

    def get_reward(self):
        return self._reward

    def is_cleared(self):
        return not self._enemy.is_alive()
