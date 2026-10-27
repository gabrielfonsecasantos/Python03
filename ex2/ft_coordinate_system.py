import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts: list[str] = []
        current: str = ""
        parts_count: int = 0

        for char in user_input:
            if char == ' ':
                continue
            elif char == ',':
                parts = parts + [current]
                parts_count += 1
                current = ""
            else:
                current = current + char

        parts = parts + [current]
        parts_count += 1

        if parts_count != 3:
            print("Invalid syntax")
            continue

        has_error: bool = False
        for number in parts:
            try:
                float(number)
            except ValueError as e:
                print(f"Error on paramenter '{number}': {e}")
                has_error = True
                break

        if has_error:
            continue

        x: float = float(parts[0])
        y: float = float(parts[1])
        z: float = float(parts[2])

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    center: float = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(center, 4)}\n")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dx: float = pos2[0] - pos1[0]
    dy: float = pos2[1] - pos1[1]
    dz: float = pos2[2] - pos1[2]
    distance_2_pts: float = math.sqrt(dx**2 + dy**2 + dz**2)
    print(f"Distance between the 2 sets of coordinates:"
          f"{round(distance_2_pts, 4)}")


if __name__ == "__main__":
    main()
