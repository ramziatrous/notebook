from flask import Flask
application = Flask(__name__)
app=application


@application.route('/')
def Hello_world():
    return 'sup. subscribe'
