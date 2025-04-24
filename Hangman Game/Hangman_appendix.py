import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words_list = [
    "apple", "banana", "camera", "dolphin", "elephant", "forest", "galaxy", "hammer", "igloo", "jacket",
    "kingdom", "lemonade", "monster", "notebook", "octopus", "pirate", "quilt", "rainbow", "spaceship", "treasure",
    "universe", "volcano", "wizard", "xylophone", "yoga", "zebra", "anchor", "bicycle", "castle", "dragon",
    "eagle", "firefly", "garden", "horizon", "island", "jellyfish", "koala", "lantern", "magic", "necklace",
    "ocean", "puzzle", "rocket", "snowflake", "thunder", "umbrella", "vampire", "waterfall", "xenon", "yarn",
    "zipper", "acrobat", "blizzard", "canyon", "dentist", "emerald", "festival", "giraffe", "hurricane", "iceberg",
    "jungle", "kangaroo", "lighthouse", "meteor", "ninja", "oasis", "parrot", "quartz", "rescue", "safari",
    "tornado", "unicorn", "vulture", "whirlpool", "adventure", "blueprint", "crocodile", "dimension", "energy", "fortress",
    "goblin", "hacker", "illusion", "justice", "knowledge", "labyrinth", "mechanic", "nightmare", "orbit", "pharaoh",
    "quest", "robot", "satellite", "timezone", "universe", "villain", "warrior", "xenophobia", "yawning", "zeppelin"
]