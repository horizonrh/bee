#/bin/python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:@localhost/bee'

db = SQLAlchemy(app)

@app.route('/')
def index():
	return "Hello bee"

if __name__ == '__main__':

	db.create_all()
	
	app.run(debug = True)
	