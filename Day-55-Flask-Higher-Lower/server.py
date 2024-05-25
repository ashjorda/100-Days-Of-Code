from flask import Flask
import random

app = Flask(__name__)

random_number = 0
for i in range(1, 9):
    random_number = random.randrange(9)

print(random_number)


def font_color(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"

    return wrapper


@app.route("/")
def start():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />")


@app.route("/<int:number>")
def guess(number):
    if number == random_number:
        return ("<h1 style='color:green;'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")
    elif number > random_number:
        return ("<h1 style='color:purple;'>Too high, try again!</h1>"
                "<br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    elif number < random_number:
        return ("<h1 style='color:red;'>Too low, try again!</h1>"
                "<br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")


if __name__ == "__main__":
    app.run(debug=True)
