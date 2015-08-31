from models.feed import Feed
from db.connection import db_session

class FeedManager():

	def publish(self, feedEntity):
		pass

	def delete(self, id):
		pass

	def viewFeed(self, id):
		result = db_session.execute('select * from feed where id=:id',{'id':id})
		feeds = result.fetchall()
		print feeds
		return feeds[0]['content']

	def feeds(self, start, size):
		pass

