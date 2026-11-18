
from player import Player
from enemy import Enemy, Boss
from weapon import Weapon
from room import Room


class Game:
    def __init__(self, player_name):
        self.__player = Player(player_name)

        self.__rooms = [
            Room(
                "Room 1 - The Slime Cave",
                "A dark cave filled with strange creatures.",
                Enemy("Slime", 30, 8)
            ),

            Room(
                "Room 2 - The Skeleton Hall",
                "An old hall guarded by a skeleton warrior.",
                Enemy("Skeleton", 45, 12),
                Weapon("Steel Sword", 25)
            ),

            Room(
                "Room 3 - The Dragon's Lair",
                "A huge dragon is protecting the treasure!",
                Boss("Dragon", 80, 15, 25)
            )
        ]

    def show_status(self):
        print("\n--- PLAYER STATUS ---")
        print("Name:", self.__player.get_name())
        print("Health:", self.__player.get_health())
        print("Weapon:", self.__player.get_weapon().get_name())
        print("---------------------")

    def play_room(self, room):
        room.enter()
        enemy = room.get_enemy()

        while enemy.is_alive() and self.__player.is_alive():

            self.show_status()

            print("\nWhat do you want to do?")
            print("1. Attack")
            print("2. Defend")
            print("3. Use potion")

            choice = input("Choose (1-3): ")

            if choice == "1":
                self.__player.attack(enemy)

            elif choice == "2":
                self.__player.defend()

            elif choice == "3":
                self.__player.use_potion()

            else:
                print("Invalid choice. Try again.")
                continue

            if enemy.is_alive():
                enemy.attack_player(self.__player)

        if not self.__player.is_alive():
            return False

        print(f"\nYou defeated {enemy.get_name()}!")

        reward = room.get_reward()

        if reward is not None:
            print("You found a new weapon!")
            self.__player.equip_weapon(reward)

        return True

    def start(self):
        print("\nWELCOME TO DUNGEON ADVENTURE!")
        print("Your mission is to defeat the dragon.")

        for room in self.__rooms:

            if not self.play_room(room):
                print("\nGAME OVER!")
                return

        print("\nCONGRATULATIONS!")
        print("You defeated the dragon and found the treasure!")
        print("YOU WIN!")

        self.show_status()
