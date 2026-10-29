import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    args: list[str] = sys.argv[1:]

    for arg in args:
        colon_idx: int = -1
        
        for i in range(len(arg)):
            if arg[i] == ":":
                colon_idx = i
                break

        if colon_idx == -1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = arg[:colon_idx]
        qty_str: str = arg[colon_idx + 1:]

        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty: int = int(qty_str)
            inventory[item] = qty
        except ValueError:
            print(f"Quantity error for '{item}': invalid literal for int() with base 10: '{qty_str}'")
            continue

    print(f"Got inventory: {inventory}")
    
    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    total_items: int = len(inventory.keys())
    print(f"Total quantity of the {total_items} items: {total_qty}")

    for item in item_list:
        qty_item: int = inventory[item]
        pct: float = 0.0
        if total_qty > 0:
            pct = (qty_item / total_qty) * 100
        print(f"Item {item} represents {round(pct, 1)}%")

    most_item: str = ""
    most_qty: int = -1
    least_item: str = ""
    least_qty: float = float('inf') 

    for item in item_list:
        qty_check: int = inventory[item]
        if qty_check > most_qty:
            most_qty = qty_check
            most_item = item
        if qty_check < least_qty:
            least_qty = qty_check
            least_item = item

    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()