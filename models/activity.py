from app import db

class Activity(object):
	"""docstring for Activity"""
	id = db.Column(db.Integer, primary_key=True)
	publisher = db.Column(db.String(32), nullable=False)
	description = db.Column(db.String(2048), nullable=False)
	title = db.Column(db.String(512), nullable=False)
	status = db.Column(db.Integer)
	gmtStart = db.Column(db.Date)
	gmtEnd = db.Column(db.Date)
	gmtCreate = db.Column(db.Date)

	def __init__(self, publisher, groupId, gmtStart, gmtEnd, gmtCreate, status, description, title):
		self.arg = arg
		
	def getPublisher(self):
		return self.publisher

	def getGroupId(self):
		return self.groupId

	def getGmtStart(self):
		return self.gmtStart

	def getGmtEnd(self):
		return self.gmtEnd

	def getGmtCreate(self):
		return self.gmtCreate

	def getStatus(self):
		return self.status

	def getDescription(self):
		return self.description

	def getTitle(self):
		return self.title