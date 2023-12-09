# Quizzler App

This Python project implements a simple quiz application called "Quizzler." The application fetches questions from the Open Trivia Database API, and users can answer True/False questions interactively.

## Installation

Ensure you have Python (version 3.x) installed on your machine. Additionally, install the required dependencies using the following command:

```bash
pip install requests
```

## Usage

Run the main quiz application script using the following command:

```bash
python main.py
```

This script will fetch questions from the Open Trivia Database API, create a quiz, and present the questions to the user with a graphical user interface.

![2023-12-01 20 45 03](https://github.com/ashjorda/100-Days-Of-Code/assets/40682488/2cb81c8c-550f-4c49-bd1f-f3c0b6e6f577)

## Project Structure

### `quiz_app.py`

This script is the main entry point for the quiz application. It fetches questions from the Open Trivia Database API, creates a quiz, and initializes the graphical user interface.

### `question_model.py`

Defines the `Question` class representing a quiz question.

### `data.py`

Fetches quiz questions from the Open Trivia Database API.

### `quiz_brain.py`

Implements the `QuizBrain` class, which manages the quiz state, tracks the user's score, and checks user answers.

### `ui.py`

Implements the `QuizInterface` class, providing the graphical user interface for the quiz.

## Acknowledgments

- The quiz application uses the Open Trivia Database API to fetch quiz questions.
- The graphical user interface is implemented using the Tkinter library.

Feel free to explore and modify the code according to your needs. Happy quizzing!

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ashjorda/100-Days-Of-Code/blob/master/LICENSE) file for details.
