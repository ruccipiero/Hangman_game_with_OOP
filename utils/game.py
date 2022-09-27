import random
from typing import List

  
class Hangman:
  """Class defining a calssic Hangman game, it basicly select a number word and gives you 5 lives 
  to try to guess the right word.
  the attributes are:
    - possible_words
    - word_to_find
    - lives
    - correctly_guessed_letters
    - well_guessed_letters
    - turn_count
    - _error_count
    the methods are:
    - play
    - start_game
    it has been tested on Python 3.10.4 and requires to import random libraries
    """    
  # possible_words contains a list of words. Out of these words, one will be selected as the word to find. 
  possible_words:List[int] = ['becode', 'learning', 'mathematics', 'sessions']

  def __init__(self):
    # word_to_find contains a list of strings. Each element will be a letter of the word.
    self.word_to_find:List[int] = list(random.choice(Hangman.possible_words))
    # A `lives` attribute that contains the number of lives that the player still has left. 
    self.lives = 5 
    # A `correctly_guessed_letters` attribute that contains a list of strings where each element 
    # is an underscore "_" but will be replaced by letter well guessed by the user. 
    self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
    # wrongly_guessed_letters` attribute contains a list of strings where each element will be a letter 
    # guessed by the user that is not in the `word_to_find`.
    self.wrongly_guessed_letters:List[int] = []
    #`turn_count` attribute contain the number of turns played by the player. 
    self.turn_count = 0
    # `error_count` attribute contains the number of errors made by the player.
    self.error_count = 0

  def play(self):
    """The `play()` method that asks the player to enter a letter. 
    the player shouldn't be allowed to type something else than a letter, 
    and not more than a letter. If the player guessed a letter well, 
    it is added to the `well_guessed_letters` list. 
    If not, it is added to the `wrongly_guessed_letters` list, the player loses a life and 1 is added to `error_count`. """
    input_letter = input("Guess one letter! - ")
    # isalpha is used to limit the input to just normal characters
    if not input_letter.isalpha():
      print("Error! Only letters a-z allowed!")
      self.play()
    # the lenght is evaluated to limit the input to just one normal characters
    elif len(input_letter) > 1:
      print("Error! Only 1 character allowed!")
      self.play()
    # an error is counted if the letter has already been guessed but you don't lose a life 
    elif input_letter in self.correctly_guessed_letters or input_letter in self.wrongly_guessed_letters:
      print(input_letter+"? you alredy tried this letter!")
      self.error_count += 1
    # if the letter is right, it is appended to the well_guessed_letters list and displayed 
    else:
      if input_letter in self.word_to_find:
        for index in range(len(self.correctly_guessed_letters)):
          if self.word_to_find[index] == input_letter:
            #Each time the player finds a letter, replace the `_` with the letter that the user suggested. 
            self.correctly_guessed_letters[index] = input_letter
      #if the letter is wrong the player loses a life and gets an error
      else:
        print("Wrong letter.")
        self.wrongly_guessed_letters.append(input_letter)
        self.error_count += 1
        self.lives -= 1
   
  def start_game(self):
    """The start_game() method that initializes all the useful variables, 
    calls the play() method as long as the player has lives
    calls te Well_done method if the player wins the game
    and calls the game_over() method if the player loses the game"""
    print('Welcome in the hangman game!')
    print("lives:",self.lives,", errors:",self.error_count,", wrong guessed:",self.wrongly_guessed_letters,", word:",self.correctly_guessed_letters )
    # the game is an endless loop that you can exit if you either win or lose 
    while True:
      # if there are no more letters to guess, the player wins and the well_played() method is runned 
      if '_' not in self.correctly_guessed_letters:
        self.well_played()
        break

      # when the lives attribute is equal to 0 game_over()method is called.
      if self.lives == 0:
        self.game_over()
        break

      # well_guessed_letters, bad_guessed_letters, life, error_count and turn_count are updated and displayed at the end of each turn.
      self.turn_count += 1
      self.play()
      print("lives:",self.lives,", errors:",self.error_count,
      ", wrong guessed:",self.wrongly_guessed_letters,", word:",self.correctly_guessed_letters )

  def well_played(self):
    """the well_played method will print 
    `You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!`. """
    print(f"You found the word: {''.join(self.correctly_guessed_letters)} in {self.turn_count} turns with {self.error_count} errors!")

  def game_over(self):
    """A game_over() method that will stop the game and print `game over...` """
    print("game over...")

# this snippet will be used for testing
if __name__ == '__main__': 
  hangman = Hangman()
  hangman.start_game()
