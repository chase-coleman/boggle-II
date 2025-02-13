# You should re-use and modify your old BoggleBoard class to support the new requirements
import random

class BoggleBoard:
  list_of_words = []
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
    word1 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    word2 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    word3 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    word4 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    vertical_word1 = "".join(word1[0] + word2[0] + word3[0] + word4[0])
    vertical_word2 = "".join(word1[1] + word2[1] + word3[1] + word4[1])
    vertical_word3 = "".join(word1[2] + word2[2] + word3[2] + word4[2])
    vertical_word4 = "".join(word1[3] + word2[3] + word3[3] + word4[3])
    BoggleBoard.list_of_words.extend([word1, word2, word3, word4])
    BoggleBoard.list_of_words.extend([word1[::-1], word2[::-1], word3[::-1], word4[::-1]])
    BoggleBoard.list_of_words.extend([vertical_word1, vertical_word2, vertical_word3, vertical_word4])
    BoggleBoard.list_of_words.extend([vertical_word1[::-1], vertical_word2[::-1], vertical_word3[::-1], vertical_word4[::-1]])
    print(word1)
    print(word2)
    print(word3)
    print(word4)


  def shake(self, word):
    while True:
      user_input = input("Do you want to shake?: ").lower()
      if user_input == 'quit':
        break
      elif user_input == "yes":
        self.print_random()
        self.include_word(word)
      elif user_input == 'no':
        self.print_blank()
  
  def include_word(self, word):
      if word in BoggleBoard.list_of_words:
        print(f"{word} has a match!")
      else:
        print(f"{word} has no matches. Try again!")
      


first = BoggleBoard()
# first.print_blank()
first.shake('bear')
first.include_word('bear')
