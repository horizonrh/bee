from app import db

class Feed(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String(32), nullable = False)
	content = db.Column(db.String(2048), nullable = False)
	status = db.Column(db.Integer)
	status = db.Column(db.Date)

	def __init__(self, author, content, status, gmtCreate):
		self.auther = author
		self.content = content
		self.status = status
		self.gmtCreate = gmtCreate

	def getAuthor(self):
		return self.author

	def getContent(self):
		return self.content

	def getStatus(self):
		return self.status

	def getGmtCreate(self):
		return self.gmtCreate