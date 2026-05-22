from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')

    # Basic Validation
    if not name or not message:
        return "Error: All fields are required!"

    return render_template('result.html', name=name, message=message)


if __name__ == '__main__':
    app.run(debug=True)