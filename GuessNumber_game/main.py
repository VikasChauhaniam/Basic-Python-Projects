from art import logo
import random

print(logo)

print("Welcome to the NumberGuessing Game!")
print("I'm thinking of a  Number between a and 100.")

attempts = 0
actual_number = random.randint(1,100)
print(f"actual number is:::::::::{actual_number}")


def game_mode():
  """Decide difficulty level of game, return 10 for easy and 5 for hard """
  
  mode = input("Choose a difficulty. Type 'easy' or 'hard' : ")
  
  if mode == 'easy':    return 10 
  elif mode == 'hard':  return 5 
  else:    print("Invalid input...")
    
def check_answer(guess_number,attempts):
  """checks if guess is correct and return attempts remaining"""
  
  if guess_number== actual_number:
    print(f"You got it! The answer was {guess_number}.")
    return -1
  elif guess_number > actual_number:
    print("Too high.")
    return attempts - 1
  else:
    print("Too low.")  
    return attempts - 1

    
def guess(attempts):
  guess_number = 0
  
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess_number = int(input("Make a guess: "))

  attempts = check_answer(guess_number,attempts)
  if attempts > 0:
    print("Guess again.\n")
    guess(attempts)

  elif attempts == 0 :
    print("\nYour've run out of guesses, you lose.")
    
  else: print("\nGame Over.")
    


guess(game_mode())
  


  

  
  