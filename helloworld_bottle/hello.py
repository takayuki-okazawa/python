__author__ = 'okazawa'

from bottle import route,run

@route('/hello')
def hello():
    return "Hello Buttle World"

run(host='localhost', port="8080", debug=True)