from flask import Flask
application = Flask(__name__)

@application.route('/')
def Hello_world():
    return 'sup. subscribe'