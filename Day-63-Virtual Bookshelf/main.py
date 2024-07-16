from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        book = {
            "title": request.form.get('Book Name'),
            "author": request.form.get('Book Author'),
            "rating": request.form.get('Rating'),
        }
        all_books.append(book)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True, port=8001)
