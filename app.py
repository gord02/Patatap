from flask import Flask

# intilalizies flask app
app = Flask(__name__)

# creates one(home) route
@app.route("/")
def hello_world():
	return "hello WOlrd"

# runs program
if __name__ == '__main__':
	app.run()