from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


def agify(name):
    """Function that takes name as an input, and using the agify.io api to return a guessed age"""
    api_url = f"https://api.agify.io/?name={name}&country_id=US"
    age = requests.get(api_url)
    if age.status_code == 200:
        return age.json()['age']
    else:
        return age.status_code


def genderize(name):
    """Function that takes name as an input, and using the genderize.io api to return a guessed gender"""
    api_url = f"https://api.genderize.io/?name={name}&country_id=US"
    gender = requests.get(api_url)
    if gender.status_code == 200:
        return gender.json()['gender']
    else:
        return gender.status_code


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    copyright_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=copyright_year)


@app.route('/guess/<string:name>')
def guess(name):
    upper_name = name.title()
    guessed_age = agify(name)
    guessed_gender = genderize(name)
    return render_template("guess.html", user=upper_name, age=guessed_age, gender=guessed_gender)


if __name__ == "__main__":
    app.run(debug=True, port=8001)
