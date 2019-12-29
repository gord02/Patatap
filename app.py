from flask import Flask, make_response, render_template, request

# intilalizies flask app(server)
app = Flask(__name__)

# creates one (index) route
@app.route("/", methods=['GET', 'POST'])
def index():
	# checks if request was GET request, if so makes respones of error type code(number)
	if request.method == 'GET':
		return make_response(render_template('index.html'), 200)

	# else not needed cause return is skipped, makes a log of info and return reposne to user
	app.logger.error("Request of type: " + request.method + " isnt handled by this route.")
	return make_response("Error", 400)

# a route to catch all other undefined routes
@app.route("/<path:path>", methods=['GET'])
def catch_all(path):
	# add a error log message when this route is accessed
	app.logger.error("User trying to access undefined route")
	return make_response(
		render_template('error.html'), 404)

# runs program
if __name__ == '__main__':
	app.run()