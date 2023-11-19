#Import both Logos for the game, and game data
import art
from game_data import data
import random
from replit import clear

#chose random choice to start the game
def random_int():
  return random.randint(0, len(data) - 1)

def check_answer(choice_a, choice_b):
  """
  Compares the follower count for Choice A, and Choice B. Then compares it to what the plaer entered. Then returns 
  """
  a = int(data[choice_a]["follower_count"])
  b = int(data[choice_b]["follower_count"])
  answer = ""
  
  if a > b:
    answer = 'a'
  elif a < b:
    answer = 'b'
  
  return answer

def upper_lower_game():
  #Set end_game condition for while loop, and sets the starting score to 0
  end_game = False
  score = 0

#Sets choice_a random variable before the game starts replacing choice_a with choice_b if the player gets the answer right. 
  choice_a = random_int()

#Makes sure the plaer can keep guessing, while loop will stop when end_game = True. Which means the player supplied a wrong answer
  while not end_game:
    clear()
    print(art.logo)
    if score > 0:
      print(f"You guessed right! Score: {score}")
  
    #Assign random integer to call a dictionary value for choice_a
    #choice_a = random_int()

  #print choice_b values
    print("Compare A: " + data[choice_a]["name"] + ", " + "a " + data[choice_a]["description"] + ", from" + data[choice_a]["country"] + ".")
    print(data[choice_a]["follower_count"])
  
    #print out the vs. ascii art
    print(art.vs)
  
    #Assign random integer to call a dictionary value for choice_b. Make sure       #it's not the same as choice_a interger
    choice_b = random_int()
  
    #Check to make sure random_int for choice_a is not equal to choice_b
    #If it's the same interger number, then choose another randome number
    if choice_a == choice_b:
      choice_b = random_int()
  
    #Print choice_b values
    print("Against B: " + data[choice_b]["name"] + ", " + "a " + data[choice_b]["description"] + ", " + "from " + data[choice_b]["country"] + ".")
    print(data[choice_b]["follower_count"])
  
    #Ask user to enter A or B
    user_choice = input("Who has more followers? Type 'A' or 'B':")
  
    #Compare the user's answer against the correct answer
    if user_choice == check_answer(choice_a, choice_b):
      score += 1
      choice_a = choice_b
    else:
      clear()
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      end_game = True
  
#start the game
upper_lower_game()



    


  
  
  
  