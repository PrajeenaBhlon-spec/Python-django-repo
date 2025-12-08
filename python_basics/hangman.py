import random
import sys


task = ["kangaroo" , "additive" , "hangman" , "notorious","fabulous" , "celestial"]
random_word = random.choice(task)
def play():
  count = 0
  for i in random_word:
    print("_ ",end="")
  print()
  print()
  
  i=0
  guessed_letter = []
  display_word = ["_ "] * len(random_word)
  while i < 25:
    guess_letter = input("guess a letter: ")
    print()
    for l in guessed_letter:
      if guess_letter == l:
        print("this letter was already guessed")
        break
    guessed_letter.append(guess_letter)
    if guess_letter not in random_word:
      count = count + 1
      check(count)

    display_index = 0
    for match_letter in random_word:
      if guess_letter == match_letter:
        display_word[display_index] = guess_letter    
        guessed_word = "".join(display_word) 
        if guessed_word == random_word:
          sys.exit("you winn🥳")

      display_index += 1
    for letter in display_word:
      print(letter,end="")
    print()
    i  = i+1

def check(c):
  if c == 1:
    print("Only 4 chance left⌛")
    print()
  if c == 2:
    print("Only 3 chance left⌛")
    print()
  if c == 3:
    print("Only 2 chance left⌛")
    print()
  if c == 4:
    print("Only 1 chance left⌛")
    print()
  if c == 5:
    print("The word is:" , random_word)
    sys.exit("game overrr💀")

play()