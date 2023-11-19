from turtle import Turtle

import pandas
import pandas as pd


class GameLogic:

    def __init__(self):
        self.file = pd.read_csv("50_states.csv")
        self.df = pd.DataFrame(self.file)
        self.correct_answers = []

    def check_state(self, answer):
        states = self.df['state'].values.tolist()
        return answer in states

    def write_state_to_map(self, state):
        x_coordinate = self.df.loc[self.df.state == state, 'x'].values[0]
        y_coordinate = self.df.loc[self.df.state == state, 'y'].values[0]
        stamp = Turtle()
        stamp.hideturtle()
        stamp.penup()
        stamp.goto(x=x_coordinate, y=y_coordinate)
        stamp.write(f"{state}", align="center")

    def populate_correct_answer_list(self, correct_answer):
        self.correct_answers.append(correct_answer)

    def work_on_list(self):
        if len(self.correct_answers) != 50:
            missed_states = [state for state in self.df.state if state not in self.correct_answers]
            study_list = pandas.DataFrame(missed_states)
            study_list.to_csv("missed_states.csv")
