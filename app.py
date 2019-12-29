from flask import Flask, render_template

# intilalizies flask app(server)
app = Flask(__name__)

# creates one (index) route
@app.route("/")
def index():
	return render_template('circles.html')

@app.route("/error")
def error():
	return render_template('error.html')

# runs program
if __name__ == '__main__':
	app.run()