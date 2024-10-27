from flask import Flask, render_template, request
from markupsafe import Markup
import markdown
import os

app = Flask(__name__)

@app.context_processor
def utility_processor():
    return dict(request=request)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for the projects page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Route for the blog page
@app.route("/blog")
def blog():
    # Specify the path to the 'blogs' folder relative to app.py
    blog_folder = os.path.join(os.path.dirname(__file__), "blogs")
    posts = []
    for filename in os.listdir(blog_folder):
        if filename.endswith(".md"):
            with open(os.path.join(blog_folder, filename), "r") as file:
                content = file.read()
                html_content = Markup(markdown.markdown(content))
                posts.append({"title": filename[:-3], "content": html_content})
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
