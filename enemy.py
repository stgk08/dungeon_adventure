
from character import Character


class Enemy(Character):
    def __init__(self, name: str, health: int, damage: int):
        super().__init__(name, health)
        self.damage = damage

    def attack(self, player):
        player.take_damage(self.damage)
        print(f"{self.get_name()} attacked you and dealt {self.damage} damage!")


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 5)


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 30, 8)


class Boss(Enemy):
    def __init__(self):
        super().__init__("Dragon", 60, 12)
