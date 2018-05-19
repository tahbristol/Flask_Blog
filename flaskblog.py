from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd65cee974fbbc376f5d5866c69dade58'

posts = [
	{
		'author': 'Tyler B.',
		'title': 'Block Post 1',
		'content': 'First post content',
		'date_posted': 'May 19, 2018'
	},
	{
		'author': 'Ali B.',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'May 19, 2018'
	}
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title="About")

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', form=form)
	
@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
	
if __name__ == '__main__':
	app.run(debug=True)