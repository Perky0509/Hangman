import random

"""A game of hangman that is layed out as a class with method functions to ask the player for a letter and check their guess. 
The word to be guessed is selected randomly from a pre-created list. Each time a guess is wrong the player loses one of 5 lives."""
class Hangman:

        #Initialising the class, setting the number of lives at the start of the game to 5 and creating a game board to visualise the players results  
        def __init__(self, word_list, num_lives = 5):
            self.word_list = word_list
            self.num_lives = num_lives
            self.random_word =  random.choice(self.word_list)
            self.word_guessed = ['_'] * len(self.random_word)
            self.num_letters = len(self.random_word)
            self.list_of_guesses = []  
        
        #If the letter guessed is in the random word, the number of letters to guess decreases by one. Otherwise the player loses a life
        def check_user_guess(self, user_letter_guess):
            if user_letter_guess in list(self.random_word):
                print(f"Good guess! {user_letter_guess} is in the word.")
                for l, letter in enumerate(self.random_word):
                    if l == user_letter_guess:
                         self.word_guessed[i] = l  
                self.num_letters -= 1          
            else: 
                self.num_lives -= 1
                print(f"Sorry, {user_letter_guess} is not in the word. Try again.")
                print(f"you have {self.num_lives} lives left")
                return self.random_word

        #This ensures that the guess made by the player is a single alphabetical character (rather than multiple characters or a number/symbol). Also checking if the player has already tried a letter (if so they don't lose a life, just prompted)
        def ask_for_input(self):
            print(self.word_guessed)
            while True:
                user_letter_guess = input(f'Please enter a sinlge letter:').lower()
                if user_letter_guess.isalpha() and len(user_letter_guess) != 1:
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif user_letter_guess in self.list_of_guesses:
                    print("You have already tried that letter!")      
                else:
                    self.check_user_guess(user_letter_guess)
                    self.list_of_guesses.append(user_letter_guess)
                    break 
                     
#Outside of the class - this function uses the class of methods to play the game         
def play_game(word_list): 
    game = Hangman(word_list, num_lives = 5) 
    while game.num_lives > 0:
        game.ask_for_input()
        if game.num_lives == 0:
            print("Game Over! You lost.")
            return game.random_word
        elif game.num_lives != 0 and game.num_letters == 0:
            return "Congratulations, you have one the game!"
                 
                      
game = Hangman(['melon', 'grapes', 'strawberries', 'figs', 'pear'])

print(play_game(game.word_list))
