from game import Game


def main():
    print("==============================")
    print("      DUNGEON ADVENTURE")
    print("==============================")

    name = input("Enter your character's name: ")

    game = Game(name)
    game.start()


if __name__ == "__main__":
    main()
