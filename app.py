from flask import Flask, render_template
from flask_mail import Mail
import datetime

app = Flask(__name__)


now = datetime.datetime.now()
current_time = now.strftime(" %I:%M %p")
current_date = now.strftime("%a %b %d ")



@app.route("/")
def hello():
    return render_template("moyemoye.html",time=current_time, date=current_date)


@app.route("/home")
def home():
    return render_template("home.html",time=current_time, date=current_date)

@app.route("/about")
def about():
    return render_template("about.html",time=current_time, data=current_date)

if __name__ == "__main__":
    app.run(debug=True)
