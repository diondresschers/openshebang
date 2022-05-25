# here is going to be the logic of the app

from flask import render_template
from app import app # The first 'app' is the directory, the second 'app' is the instantatiation from the __init__.py file.

@app.route('/') # This is a decorator and will connect an URL with a function
@app.route('/index')
def index():
    user = {'username': 'Dion'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Don\'t worry',

        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) # The 'render_template' still have be imported. Flask will look by default in the 'templates' folder (in the 'app'-section). The first 'user' is going to be the 'user' in the template and the second 'user' is the Python Dictionary.



