from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(debug=True)