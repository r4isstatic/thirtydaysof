from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello and welcome to Thirty Days of..."

	