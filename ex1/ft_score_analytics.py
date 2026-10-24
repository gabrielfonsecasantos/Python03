import sys

def main() -> None:
  print("=== Player Score Analytics ===")

  args: list[str] = sys.argv[1:]
  scores: list[int] = []

  for arg in args:
    try:
      score = int(arg)
      scores = scores + [score]
    except ValueError:
      print(f"Invalid parameter: '{arg}'")

  if len(scores) == 0:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1>, <score2> ...")
    return

  total_players: int = len(scores)
  total_score: int = sum(scores)
  average_score: float = total_score / total_players
  highest_score: int = max(scores)
  lowest_score: int = min(scores)
  score_range: int = highest_score - lowest_score

  print(f"Scores processed: {scores}")
  print(f"Total players: {total_players}")
  print(f"Total score: {total_score}")
  print(f"Average score: {average_score}")
  print(f"High score: {highest_score}")
  print(f"Lowest score: {lowest_score}")
  print(f"Score range: {score_range}")

if __name__ == "__main__":
  main()