from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_post = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()


@app.route('/')
def index():
    return render_template("index.html", blogs=blog_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:id>')
def post(id):
    blog = blog_post[id-1]
    return render_template("post.html", blog_post=blog)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
