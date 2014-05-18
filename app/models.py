from app import db

class Blogger(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(200), index = True, unique = False)
	url = db.Column(db.String(200), index = True, unique = False)
	choices = db.relationship('Choice', backref = 'b_choice', lazy = 'dynamic')

	def __repr__(self):
		return 'Blogger name %r>' % (self.name)

class Question(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300), index = True, unique = False)
	day = db.Column(db.Integer, index = True, unique = False)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	choices = db.relationship('Choice', backref = 'q_choice', lazy = 'dynamic')

	def __repr__(self):
		return 'Question title %r>' % (self.title)

class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(200), index = True, unique = False)
	questions = db.relationship('Question', backref = 'question', lazy = 'dynamic')

	def __repr__(self):
		return 'Category name %r>' % (self.name)

class Choice(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	url = db.Column(db.String(300), index = True, unique = False)
	title = db.Column(db.String(300), index = True, unique = False) #eventually pull this out into a separate class of 'Song' and so on
	year = db.Column(db.String(4), index = True, unique = False)
	blogger_id = db.Column(db.Integer, db.ForeignKey('blogger.id'))
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

	def __repr__(self):
		return 'Choice title %r>' % (self.title)
