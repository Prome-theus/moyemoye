import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_mail import Mail, Message
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from flask_login import LoginManager, login_required

from forms import HiremeForm

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://rockbottom0111:0iGRT5lPNMLIRskC@cluster0.lmyxnuh.mongodb.net/local'
app.config['SECRET_KEY'] = '6e6cf3f875a3a73830d88caf'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['MONGODB_SETTINGS'] = {
    'db': 'local',
    'host': 'mongodb+srv://rockbottom0111:0iGRT5lPNMLIRskC@cluster0.lmyxnuh.mongodb.net/'
}

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rockbottom0111@gmail.com'
app.config['MAIL_PASSWORD'] = 'omyb xpzn oeok mdqy'
app.config['MAIL_DEFAULT_SENDER'] = 'rockbottom0111@gmail.com'

# mongo = PyMongo(app)
mongo = MongoEngine(app)
login_manager = LoginManager(app)
admin = Admin(app, name='MyBlog', template_mode='bootstrap3')
mail = Mail(app)


class Blog(mongo.Document):
    title = mongo.StringField(max_length=200, required=True)
    content = mongo.StringField(required=True)
    image = mongo.StringField(max_length=1024, required=True)

@login_manager.user_loader
def load_user(user_id):
    # Implement this function if you are using Flask-Login and have a user model
    pass

class BlogView(ModelView):
    # Customize if needed
    pass

admin.add_view(BlogView(Blog, mongo.db))

now = datetime.datetime.now()
current_time = now.strftime(" %I:%M %p")
current_date = now.strftime("%a %b %d ")

@app.route("/")
def hello():
    return render_template("moyemoye.html", time=current_time, date=current_date)

@app.route("/admin")
@login_required
def admin():
    return render_template("moye.html")

@app.route("/home")
def home():
    return render_template("home.html", time=current_time, date=current_date)

@app.route("/about")
def about():
    return render_template("about.html", time=current_time, date=current_date)

@app.route("/blog")
def blog():
    posts = Blog.objects.all()
    return render_template("blog.html", time=current_time, date=current_date, posts=posts)

@app.route("/hireme", methods=['GET', 'POST'])
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
        flash('Message sent successfully', category="success")

        return redirect(url_for('about'))

    if form.errors:
        flash('Please enter the correct details', category="danger")

    return render_template("hireme.html", time=current_time, date=current_date, form=form)

if __name__ == "__main__":
    app.run(debug=True)
