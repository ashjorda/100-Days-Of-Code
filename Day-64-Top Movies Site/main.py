from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


class EditRating(FlaskForm):
    rating = StringField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    done = SubmitField(label="Done")


class AddMovie(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    done = SubmitField(label="Add Movie")


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Create the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[float] = mapped_column(Float, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        movie_results = result.scalars().all()
        movie_list = list(movie_results)
    return render_template('index.html', movies=movie_list)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        movie_id = request.args.get('id')
        with app.app_context():
            movie_to_update = db.get_or_404(Movie, movie_id)
            movie_to_update.rating = request.form.get('rating')
            movie_to_update.review = request.form.get('review')
            db.session.commit()
            return redirect(url_for('home'))
    edit_rating = EditRating()
    return render_template('edit.html', form=edit_rating)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    with app.app_context():
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        movie_list = []
        search_string = request.form.get('title')
        token = os.environ['token']
        headers = {
            'Authorization': token,
            'accept': 'application/json'
        }
        search = requests.get(url=f'https://api.themoviedb.org/3/search/movie?query={search_string}', headers=headers)
        search_result = search.json()
        for title in search_result['results']:
            title_id = title['id']
            original_title = title['original_title']
            title_year = title['release_date']
            movie_entry = title_id, original_title, title_year
            movie_list.append(movie_entry)
        return render_template('select.html', movie_results=movie_list)
    new_movie = AddMovie()
    return render_template('add.html', form=new_movie)


@app.route("/select")
def select():
    movie_id = request.args.get('id')
    token = os.environ['token']
    token = os.environ['token']
    headers = {
        'Authorization': token,
        'accept': 'application/json'
    }
    search = requests.get(url=f'https://api.themoviedb.org/3/movie/{movie_id}', headers=headers)
    search_result = search.json()
    with app.app_context():
        new_entry = Movie(title=search_result['original_title'], year=search_result['release_date'].split('-')[0], description=search_result['overview'], rating=None, ranking=None, review=None, img_url=f"https://image.tmdb.org/t/p/w500/{search_result['poster_path']}")
        db.session.add(new_entry)
        db.session.commit()
    db_id = db.session.execute(db.select(Movie.id).where(Movie.title == search_result['original_title'])).scalar()
    return redirect(url_for('edit', id=db_id))


if __name__ == '__main__':
    app.run(debug=True, port=8001)
