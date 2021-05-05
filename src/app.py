from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
	return "Hello World!"

@app.route("/custom")
def custom():
	return "My First CI/CD push!"

if __name__=="__main__":
	app.run()