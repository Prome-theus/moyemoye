import datetime
from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail
from forms import HiremeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6e6cf3f875a3a73830d88caf'

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
        sendername = form.name.data
        senderemail = form.email.data
        sendermsg = form.msg.data

        print(f'{sendername} from {senderemail} said {sendermsg}')
        # flash(f'msg sent successfully')

        return redirect(url_for('about'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            #flash(f'please enter the correct details')
            pass
            
    return render_template("hireme.html", time=current_time, date=current_date, form=form)

if __name__ == "__main__":
    app.run(debug=True)
