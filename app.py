#/bin/python
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

import feed
from social.feed import FeedManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bee'
db = SQLAlchemy(app)

@app.route('/api/feed/view/<int:id>', methods=['GET'])
def viewFeed(id):
	feedManager = FeedManager()
	return feedManager.viewFeed(id)

@app.route('/api/feed/publish', methods=['POST'])
def publishFeed():
	pass

@app.route('/api/feed/delete/<int:id>', methods=['POST'])
def deleteFeed(id):
	pass

@app.route('/api/feed/edit/<int:id>', methods=['POST'])
def editFeed(id):
	pass

@app.route('/api/activity/view/<int:id>', methods=['GET'])
def viewActivity(id):
	print 'Activity'

@app.route('/api/activity/publish', methods='[POST]')
def publishActivity():
	pass

@app.route('/api/activity/delete/<int:id>', methods=['POST'])
def deleteActivity(id):
	pass

@app.route('/api/activity/edit/<int:id>', methods=['POST'])
def editActivity(id):
	pass

if __name__ == '__main__':

	app.run(debug=True)

	