from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    blog_post = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    blogs = blog_post.json()
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:id>')
def post(id):
    print(id)
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
