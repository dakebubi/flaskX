# This Python file uses the following encoding: utf-8
from flask import Flask
from flask import jsonify

# mock 数据库返回信息
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run()
