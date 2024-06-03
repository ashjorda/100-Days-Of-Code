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
    """default route renders index.html with a random number, dynamic copyright year, and python expression within the
     index.html template file"""
    random_number = random.randint(1, 10)
    copyright_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=copyright_year)


@app.route('/guess/<string:name>')
def guess(name):
    """Route that takes the string from the appended url, and renders guess.html
    with title case name, guessed age, and gender"""
    upper_name = name.title()
    guessed_age = agify(name)
    guessed_gender = genderize(name)
    return render_template("guess.html", user=upper_name, age=guessed_age, gender=guessed_gender)


@app.route('/blog')
def blog():
    """Route that takes renders the results from the blog_url api within the blog.html template"""
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, port=8001)
