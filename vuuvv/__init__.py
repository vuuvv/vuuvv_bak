from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine()

if __name__ == '__main__':
    app.run()
