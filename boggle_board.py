# You should re-use and modify your old BoggleBoard class to support the new requirements
import random

class BoggleBoard:
  
  def __init__(self):
    pass

  def print_blank(self):
     msg = """
-----
-----
-----
"""
     print(msg)
  
  def print_random(self):
    print("".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower())
    print("".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower())
    print("".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower())
    print("".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower())


  def shake(self):
    while True:
      # keep_running = True
      user_input = input("Do you want to shake?: ").lower()
      if user_input == 'quit':
        break
      elif user_input == "yes":
        self.print_random()
      elif user_input == 'no':
        self.print_blank()
  
  def include_word(self):
      pass


first = BoggleBoard()
# first.print_blank()
first.shake()
