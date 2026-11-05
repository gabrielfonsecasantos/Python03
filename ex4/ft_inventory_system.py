import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("Empty inventory.")
        return

    inventory: dict[str, int] = {}

    args: list[str] = sys.argv[1:]

    for arg in args:
        colon_index: int = -1

        for i in range(len(arg)):
            if arg[i] == ":":
                colon_index = i
                break

        if colon_index == -1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = arg[:colon_index]
        quantity: str = arg[colon_index + 1:]

        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            item_quantity: int = int(quantity)
            inventory[item] = item_quantity
        except ValueError:
            print(f"Quantity error for '{item}': invalid literal for ")
            print(f"int() with base 10: '{quantity}'")
            continue

    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity: int = sum(inventory.values())
    total_items: int = len(inventory.keys())
    print(f"Total quantity of the {total_items} items: {total_quantity}")

    for item in item_list:
        quantity_item: int = inventory[item]
        percentage: float = 0.0
        if total_quantity > 0:
            percentage = (quantity_item / total_quantity) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")

    first_item = item_list[0]
    most_item: str = first_item
    most_quantity: int = inventory[first_item]
    least_item: str = first_item
    least_quantity: float = inventory[first_item]

    for item in item_list:
        quantity_check: int = inventory[item]
        if quantity_check > most_quantity:
            most_quantity = quantity_check
            most_item = item
        if quantity_check < least_quantity:
            least_quantity = quantity_check
            least_item = item

    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
