
from character import Character
from weapon import Weapon
from potion import Potion


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
