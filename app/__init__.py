from flask import Flask # only import 'Flask' 

app = Flask(__name__) # Create an instance of Flask. Use __name__, is the Python name of the app. so it can find other files. 

from app import routes # Normally importing is done in the first line, but this is to prevent Flask 'circular dependancies'. # THe `routes` has still to be created.



