import random
import typing


def gen_event(
    player_list: list[str],
    action_list: list[str]
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(player_list)
        action: str = random.choice(action_list)
        event: tuple[str, str] = (player, action)
        yield event


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        element: tuple[str, str] = random.choice(event_list)
        for item in event_list:
            if item == element:
                event_list.remove(item)
                # O ideal é usar break aqui após remover para evitar
                # comportamentos inesperados ao iterar numa lista modificada
                break
        yield element


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    player_list: list[str] = ["Alice", "Bob", "Dylan", "Charlie"]
    action_list: list[str] = [
        "swin", "sleep", "jump", "move", "run",
        "grab", "eat", "climb", "release"
    ]

    stream = gen_event(player_list, action_list)

    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event_list = event_list + [next(stream)]
    print(f"\nBuilt list of 10 events: {event_list}\n")

    for item in consume_event(event_list):
        print(f"Got event from list: {item}")
        print(f"Remains in list: {event_list}")