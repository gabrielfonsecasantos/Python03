import random

def gen_player_achievements() -> set[str]:
  achievements_list: set[str] = {
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner", "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable", "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind", "Boss Slayer", "Hidden Path Finder"
  }

  new_set = rand