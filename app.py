import datetime
from flask import Flask, render_template
from flask_mail import Mail
from forms import HiremeForm

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
    return render_template("about.html",time=current_time, date=current_date)

@app.route("/hireme")
def hireme():
    form = HiremeForm()
    if form.validate_on_submit():
        pass
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'please enter the correct details')
            
    return render_template("hireme.html", time=current_time, date=current_date)

if __name__ == "__main__":
    app.run(debug=True)
