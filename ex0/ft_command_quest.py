import sys

def print_args(argv: list) -> None:
  list = argv
  print(f"Program name: {list[0]}")
  if len(list) == 1:
    print("No arguments provided!")
    print(f"Total arguments: {len(list)}")
    return
  print(f"Arguments received: {len(list) - 1}")
  i = 1
  while(i < len(list)):
    print(f"Argument {i}: {list[i]}")
    i += 1
  print(f"Total arguments: {len(list)}")

if __name__ == "__main__":
    print("=== Command Quest ===")
    print_args(sys.argv)