#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<h2>"hello": {param}</h2>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return f'<h2>Counting numbers up to {param}:</h2><pre>{numbers}</pre>'

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'<h2>Result of {num1} {operation} {num2} is:</h2><p>{result}</p>'
    else:
        return '<h2>Error: Invalid operation or division by zero</h2>'

if __name__ == '__main__':
    app.run(debug=True)
