from utils.game import Hangman

hangman = Hangman()
hangman.start_game()

while input("Do you want to play again? (y/n) - ") == 'y':
    hangman = Hangman()
    hangman.start_game()
