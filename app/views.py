from app import app, db, models
from flask import render_template
# List of routes

# .com = homepage
# .com/categories = list of categories (music, film etc.)
# .com/:category
# .com/:category/:year = table of choices per person in that category, for that year

# there's more routes I could do (e.g. /blogger, /:category/questions and so on, but they'll come later)

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/categories')
def categorylist():
	categories = models.Category.query.all()
	return render_template("categories.html", categorylist=categories)

@app.route('/<categoryID>')
def category(categoryID):	
	category = models.Category.query.get(categoryID)
	questions = models.Question.query.filter_by(category_id=categoryID).all()
	allyears = []
	for question in questions:
		choices = models.Choice.query.filter_by(question_id=question.id).all()
		for choice in choices:
			allyears.append(choice.year)
	years = set(allyears)
	return render_template("category.html", category=category, questions=questions, years=years)

@app.route('/<categoryID>/<year>')
def yearchoices(categoryID, year):
	category = models.Category.query.get(categoryID)
	questions = models.Question.query.filter_by(category_id=categoryID).all()
	allchoices = []
	for question in questions:
		choices = models.Choice.query.filter_by(question_id=question.id, year=year).all()
		for c in choices:
			blogger = models.Blogger.query.get(c.blogger_id)
			blogger_url = blogger.url
			blogger_name = blogger.name
			question_title = question.title
			question_no = question.day
			allchoices.append({'id' : c.id, 'title' : c.title, 'url' : c.url, 'blogger_name' : blogger_name, 'blogger_url' : blogger_url, 'question_title' : question_title, 'question_no' : question_no})
	return render_template("yearchoices.html", category = category, questions = questions, choices = allchoices, year = year)
