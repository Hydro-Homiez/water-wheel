from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():

    return render_template("home.html")

@app.route("/about")
def about_page():

    return "This is the about page"

if __name__ == '__main__':

    app.run(debug=True)


