from flask import Flask, render_template, jsonify, url_for, request
import random
import secrets

flask_api = Flask(__name__)


@flask_api.route('/')
def homepage():
    session_id = secrets.token_hex()
    return render_template('index.html', session_id=session_id)

@flask_api.route('/guess_number')
def guessNum():
    rand_int = random.randint(0, 101)
    return jsonify({
        "Random_number": rand_int
    })

@flask_api.route('/get_birth_year')
def get_birth_year():

    if request.method == 'POST':
        birth_year = request.form["birth_year"]
        age = request.form["age"]

        print(age, birth_year)

        return redirect(url_for('index'))

if __name__ == '__main__':
    flask_api.run(debug=True)