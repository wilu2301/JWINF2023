"""JWINF 2023 Runde 3 Aufgabe 1: Wundertüte
Assets: https://bwinf.de/bundeswettbewerb/42/1/"""

def calculate(packages: int, games: list) -> list:
    """Calculates the amount of games per bag.
    :param packages: The amount of packages
    :param games: The amount games ordered by type
    :return: A list of lists containing the amount of games and their type per bag
    """
    bags = []

    for i in range(packages):
        game = []
        for n in range(len(games)):
            game.append(games[n] // packages)
        bags.append(game)

    for i in range(len(games)):
        games[i] = games[i] % packages

    current_bag = 0
    for i in range(len(games)):
        for n in range(games[i]):
            if games[i] <= 0:
                break

            if current_bag >= len(bags):
                current_bag = 0

            bags[current_bag][i] += 1
            current_bag += 1
            games[i] -= 1

    return bags


def main():
    """Basic CLI for the bag calculator"""

    print("[Bag Calculator] Please enter the amount of packages")
    packages: int = int(input("->"))
    if not packages:
        print("No amount entered, try again!")
        return
    print("[Bag Calculator] Please enter the amount of game-types")
    amount_games: int = int(input("->"))
    if not amount_games:
        print("No amount entered, try again!")
        return

    games = []

    for i in range(amount_games):
        print("[Bag Calculator] Please enter the amount of game-type " + str(i))
        games.append(int(input("->")))
        if not games[i]:
            print("No amount entered, try again!")
            return

    print(f"[Bag Calculator] Calculating {packages} packages with values {games} ...")
    result = calculate(packages, games)
    for i in range(len(result)):
        print(f"Package: {i}: {result[i]}")


if __name__ == "__main__":
    main()
