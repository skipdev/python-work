def over(word):
  print( "*" * len(word))
  print(word)
  
def under(word):
  print(word)
  print( "*" * len(word))

def both(word):
  print( "*" * len(word))
  print(word)
  print( "*" * len(word))
  
def grid(word, grid_size):
  print(("*" * len(word), " ") * (grid_size - 1), "*" * len(word))
  for x in range(grid_size):
      print((word, "|") * (grid_size -1), word)
      print(("*" * len(word), " ") * (grid_size - 1), "*" * len(word))
  print()