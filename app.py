import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
# from flask_sqlalchemy import Bcrypt
from flask_login import LoginManager

from forms import HiremeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '6e6cf3f875a3a73830d88caf'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rockbottom0111@gmail.com'
app.config['MAIL_PASSWORD'] = 'omyb xpzn oeok mdqy'
app.config['MAIL_DEFAULT_SENDER'] = 'rockbottom0111@gmail.com'

db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
login_manager =  LoginManager(app)
###login_manager.login_view = 'login'
###loginmessagecategory
admin = Admin(app, name='MyBlog', template_mode='bootstrap3')

mail = Mail(app)

class blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=200), nullable=False)
    content = db.Column(db.Text, nullable=False, unique=False)
    image = db.Column(db.String(length=1024), nullable=False, unique=False)


now = datetime.datetime.now()
current_time = now.strftime(" %I:%M %p")
current_date = now.strftime("%a %b %d ")


@app.route("/")
def hello():
    return render_template("moyemoye.html",time=current_time, date=current_date)

@app.route("/admin")
@login_required
def admin():
    

@app.route("/home")
def home():
    return render_template("home.html",time=current_time, date=current_date)

@app.route("/about")
def about():
    return render_template("about.html",time=current_time, date=current_date)

@app.route("/blog")
def blog():
    # page = request.args.get('page', 1, type=int)
    # item_per_page = 6
    # pagination = Item.query.paginate(per_page=item_per_page)
    # items = pagination.items
    # return render_template("blog.html", time=current_time, date=current_date, items=items, pagination=pagination)
    return render_template("blog.html", time=current_time, date=current_date)

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
