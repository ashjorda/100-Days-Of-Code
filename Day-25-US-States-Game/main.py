import turtle
from game_logic import GameLogic

# instructor shared code for adding a .gif as the background to a turtle screen
screen = turtle.Screen()
screen.title("U.S Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# instructor shared code for adding a .gif as the background to a turtle screen

# create game object from GameLogic() class
game = GameLogic()

# Loop the code to allow continuous guessing until all 50 states have been added to the map
while len(game.correct_answers) < 50:
    # score equals the length of the correct answers list populated based on correct guesses
    score = len(game.correct_answers)
    # Prompt user to guess a state, and convert entry to title case
    state_guess = screen.textinput(title=f"{score} / 50 States Correct", prompt="Enter a State name:").title()
    # If the user types "exit", write a txt file for stated not entered. Then close the application.
    if state_guess == "Exit":
        game.work_on_list()
        break

    # Check to see if a correct state is entered, then write the name of the state on the map
    # and append the state to the game.correct_answers list.
    if game.check_state(state_guess):
        game.write_state_to_map(state_guess)
        game.populate_correct_answer_list(state_guess)