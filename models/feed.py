class Feed(object):

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