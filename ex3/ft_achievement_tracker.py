import random


def gen_player_achievements() -> set[str]:
    new_set: set[str] = set()
    achievements_list: set[str] = {
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
    }

    random_num = random.randint(1, len(achievements_list))
    while len(new_set) < random_num:
        random_index = random.randint(0, 13)
        current_index = 0
        for item in achievements_list:
            if random_index == current_index:
                new_set = new_set | {item}
                break
            current_index += 1
    return new_set


if __name__ == "__main__":
    achievements_list: set[str] = {
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
    }
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")

    print(f"All distinct achievements: {achievements_list}\n")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")
    print(f"Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Dylan has: {dylan.difference(bob, charlie, alice)}\n")

    print(f"Alice is missing: {achievements_list.difference(alice)}")
    print(f"Bob is missing: {achievements_list.difference(bob)}")
    print(f"Charlie is missing: {achievements_list.difference(charlie)}")
    print(f"Dylan is missing: {achievements_list.difference(dylan)}")
    