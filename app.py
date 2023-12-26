from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    current_time = now.strftime(" %I:%M %p")
    current_date = now.strftime("%a %b %d ")
    return render_template("moyemoye.html",time=current_time, date=current_date)


if __name__ == "__main__":
    app.run(debug=True)
