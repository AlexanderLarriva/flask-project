from flask import Flask
from flask import render_template

# Это callable WSGI-приложение
app = Flask(__name__, template_folder='/home/larriva/Flask-training/templates')

@app.route('/')
def hello_world():
    return 'Welcome to Minsk!'


@app.get('/users')
def users_get():
    return 'GET /users'


# @app.post('/users')
# def users_post():
#     return 'POST /users '

@app.post('/users')
def users():
    return 'Users', 302

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'


@app.route('/users/<id>')
def get_user(id):

    return render_template(
        'show.html',
        name=id,
    )