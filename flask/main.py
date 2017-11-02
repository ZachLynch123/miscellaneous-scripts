from flask import Flask, render_template

app = Flask(__name__)


# @ is a decorator. a way to wrap a function and modifying its behavior
# routing to home page '... .com/'

@app.route("/")
@app.route("/<user>")
@app.route('/profile/<name>')
def index(user=None):
	return render_template("user.html", user=user)

@app.route("/things_to_do")
def shopping():
    food = ['love Allison', 'nap', 'love Allison']
    return render_template("shopping.html", food=food)











if __name__ == "__main__":
	app.run(debug=True)


















