"""""
In this typical case, set lookups would be roughly 100-1000x faster than list lookups. This is because:
Lists check each element one by one (O(n) time complexity)
Sets use hash tables for instant lookups (O(1) time complexity)
For a Boggle board where you're frequently checking if words exist, this difference could mean:
List: ~0.1-1 milliseconds per word check
Set: ~0.001-0.01 milliseconds per word check
While this might not matter for casual play, it would become very noticeable if you were doing something like checking all possible words on the board against a dictionary.
"""""
## Added this answer from claude.ai on why a set would be faster/more efficient that using a list

import random

class BoggleBoard:
  set_of_words = set()
  
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
    # Creates 4 random words
    word1 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    word2 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    word3 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    word4 = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)).lower()
    # Creates the 4 vertical words by using the same index from each index of the 4 horizontal words
    vertical_word1 = "".join(word1[0] + word2[0] + word3[0] + word4[0])
    vertical_word2 = "".join(word1[1] + word2[1] + word3[1] + word4[1])
    vertical_word3 = "".join(word1[2] + word2[2] + word3[2] + word4[2])
    vertical_word4 = "".join(word1[3] + word2[3] + word3[3] + word4[3])
    # Adds the horizontal words and those words in reverse to the class attribute set_of_words
    BoggleBoard.set_of_words.update([word1, word2, word3, word4, word1[::-1], word2[::-1], word3[::-1], word4[::-1]])
    # Adds the vertical words and those words in reverse
    BoggleBoard.set_of_words.update([vertical_word1, vertical_word2, vertical_word3, vertical_word4, vertical_word1[::-1], vertical_word2[::-1], vertical_word3[::-1], vertical_word4[::-1]])
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
      # print(BoggleBoard.list_of_words)
      if word in BoggleBoard.set_of_words:
        print(f"{word} has a match!")
      else:
        print(f"{word} has no matches. Try again!")
      


first = BoggleBoard()
# first.print_blank()
first.shake('bear')
first.include_word('bear')
