from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


def agify(name):
    api_url = f"https://api.agify.io/?name={name}&country_id=US"
    age = requests.get(api_url)
    if age.status_code == 200:
        return age.json()['age']
    else:
        return age.status_code


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    copyright_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=copyright_year)


@app.route('/guess/<string:name>')
def guess(name):
    upper_name = name.title()
    guessed_age = agify(name)
    return render_template("guess.html", user=upper_name, age=guessed_age)


if __name__ == "__main__":
    app.run(debug=True, port=8001)
