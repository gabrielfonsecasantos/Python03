import random


def main() -> None:
    player_names: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {player_names}")

    capitalized_names: list[str] = [
        item.capitalize() for item in player_names
    ]
    print(f"New list with all names capitalized {capitalized_names}")

    only_capitalized: list[str] = [
        item for item in player_names if item == item.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capitalized}\n")

    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in capitalized_names
    }
    print(f"Score dict: {score_dict}")

    total_score1: int = 0
    for name in score_dict:
        total_score1 += score_dict[name]
    average_score: float = 0.0
    if len(score_dict) > 0:
        average_score = round(total_score1 / len(score_dict), 2)
    print(f"Score average is {average_score}")

    high_scores: dict[str, int] = {
        name: score_dict[name] for name in score_dict
        if score_dict[name] > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    main()
