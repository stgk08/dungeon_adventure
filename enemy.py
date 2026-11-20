import random
from character import Character


class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.__damage = damage

    def attack_player(self, player):
        player.take_damage(self.__damage)

        print(
            f"{self.get_name()} attacks you "
            f"for {self.__damage} damage!"
        )


class Boss(Enemy):
    def __init__(self, name, health, damage, special_attack):
        super().__init__(name, health, damage)
        self.__special_attack = special_attack

    def special_move(self, player):
        player.take_damage(self.__special_attack)

        print(
            f"{self.get_name()} uses a SPECIAL ATTACK "
            f"for {self.__special_attack} damage!"
        )

    def attack_player(self, player):
        if random.randint(1, 3) == 1:
            self.special_move(player)
        else:
            super().attack_player(player)
