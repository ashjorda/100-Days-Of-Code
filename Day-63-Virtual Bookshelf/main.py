from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

all_books = []


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Bookshelf(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Bookshelf).order_by(Bookshelf.title))
        library_books = result.scalars()
        books = list(library_books)
    return render_template("index.html", book_list=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Bookshelf(title=request.form.get('Book Name'), author=request.form.get('Book Author'),
                                 review=request.form.get('Rating'))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<id>")
def edit(id):
    pass


if __name__ == "__main__":
    app.run(debug=True, port=8001)
