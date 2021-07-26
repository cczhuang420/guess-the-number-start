#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo

# global variavle
HARD_LEVEL = 5
EASY_LEVEL = 10

def set_difficulty():
  """Set the difficulty and return it's level """
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "hard":
    return HARD_LEVEL
  elif difficulty == "easy":
    return EASY_LEVEL

def game_start():
  print(logo)
  # Allow the player to submit a guess for a number between 1 and 100
  print("Welcome to the Number Guessing Game！")
  print("I'm thinking of a number between 1 and 100.")
  num_to_guess = random.randint(1, 100)
  
  num_attempt = set_difficulty()
  def guess_again():
    if num_attempt != 0:
      print("Guess again.")

  def answer_check(guess, answer):
    if guess > answer:
      print("To high.")
      guess_again()
    elif guess < answer:
      print("Too low.")
      guess_again()
    else:
      print(f"You got it, the answer is: {num_to_guess}")

  num_guess = 0
  while num_guess != num_to_guess:
    num_guess = int(input("Make a guess: "))
    num_attempt -= 1
    answer_check(num_guess, num_to_guess)
    print(f"You have {num_attempt} attemp(s) remaining to guess the number.")
    if num_attempt == 0: 
      print("You run out of turns, you lose.")
      return

game_start()
    
