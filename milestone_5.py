#Milestone 5 

import random

#word_list = ['melon', 'grapes', 'strawberries', 'figs', 'kiwi']
class Hangman:
        
        
        def __init__(self, word_list, num_lives = 5):
            self.word_list = word_list
            self.num_lives = num_lives
            self.random_word =  random.choice(self.word_list)
            self.word_guessed = ['_'] * len(self.random_word)
            self.num_letters = len(self.random_word)
            self.list_of_guesses = []

            
        
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

        def ask_for_input(self):
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
                     
        
def play_game(word_list): 
    game = Hangman(word_list, num_lives = 5) 
    while True:
            if game.num_lives > 0:
                game.ask_for_input()
            elif game.num_lives == 0:
                print("Game Over! You lost.")
                return game.random_word
            elif game.num_lives != 0 and game.num_letters == 0:
                return "Congratulations, you have one the game!"
                
                
                

        
game = Hangman(['melon', 'grapes', 'strawberries', 'figs', 'pear'])

print(play_game(game.word_list))
