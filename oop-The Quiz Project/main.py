from data import computer_science_data, question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

#You can change the question database by changing the list name in the for loop. Options are, computer_science_data
#or question_data
for questions in computer_science_data:
    question_bank.append(Question(questions['question'], questions['answer']))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've Completed the Quiz!\nYour final score is: {quiz.score}/{len(question_bank)}")