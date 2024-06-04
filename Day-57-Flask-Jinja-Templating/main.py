from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    if response.status_code == 200:
        blog_post = response.json()
        return render_template("index.html", blogs=blog_post)
    else:
        return render_template("index.html")


@app.route('/post/<int:num>')
def blog_post(num):
    print(num)
    blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blogs_url)
    if response.status_code == 200:
        blogs_post = response.json()[num]
        blog_title = blogs_post['title']
        blog_subtitle = blogs_post['subtitle']
        blog_body = blogs_post['body']
        return render_template("post.html", title=blog_title, subtitle=blog_subtitle, body=blog_body)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8001)
