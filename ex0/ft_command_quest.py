import sys


def print_args(argv: list[str]) -> None:
    args: list[str] = argv
    print(f"Program name: {args[0]}")
    if len(args) == 1:
        print("No arguments provided!")
        print(f"Total arguments: {len(args)}")
        return

    print(f"Arguments received: {len(args) - 1}")
    i = 1
    while i < len(args):
        print(f"Argument {i}: {args[i]}")
        i += 1
        print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    print_args(sys.argv)
