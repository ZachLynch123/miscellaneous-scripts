from flask import Flask, request

app = Flask(__name__)


# @ is a decorator. a way to wrap a function and modifying its behavior
# routing to home page '... .com/'
@app.route('/')
def index():
	return 'Method used: %s' % request.method




@app.route('/bacon', methods=['GET','POST'])
def bacon():
	return "Method used: %s" % request.method






if __name__ == "__main__":
	app.run(debug=True)


















