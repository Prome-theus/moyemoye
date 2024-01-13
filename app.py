import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_mail import Mail
from forms import HiremeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6e6cf3f875a3a73830d88caf'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'bond.james9911@gmail.com'
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)

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

@app.route("/hireme",methods=['GET', 'POST'])
def hireme():
    form = HiremeForm()
    if form.validate_on_submit():
        sname = form.name.data
        semail = form.email.data
        smsg = form.msg.data

        msg = Message('New contact Form Submission', recipients=["tanishvashisth@gmail.com"])
        msg.body = f'Name: {sname}\nEmail: {semail}\nMessage: {smsg}'
        mail.send(msg)

        print(f'{sname} from {semail} said {smsg}')
        flash(f'msg sent successfully', category="success")

        return redirect(url_for('about'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'please enter the correct details', category="danger")
            pass
        return redirect(url_for('hireme'))
            
    return render_template("hireme.html", time=current_time, date=current_date, form=form)

if __name__ == "__main__":
    app.run(debug=True)
