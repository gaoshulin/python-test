from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='123456':
        return render_template('success.html', username=username)
    
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run(debug=True)
