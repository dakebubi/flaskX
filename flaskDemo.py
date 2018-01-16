# This Python file uses the following encoding: utf-8
from flask import Flask
from flask import jsonify
from flask import request

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
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return jsonify({'tasks': tasks})


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form  # 获取POST表单数据
        username = form['username']
        password = form['password']
        print  username, password
        return "POST login success"
    else:
        args = request.args  # 获取get请求参数
        print args
        return "GET login success"

    values = request.values  # 获取所有参数
    print values


if __name__ == '__main__':
    app.run()
