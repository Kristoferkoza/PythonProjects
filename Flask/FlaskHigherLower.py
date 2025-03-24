from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

@app.route('/<int:number>')
def guess(number):
    if number == random_number:
        return "<h1>It is the correct guess!</h1>" \
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
    elif number < random_number:
        return "<h1>It is too low!</h1>" \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    else:
        return "<h1>It is too high!</h1>" \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"

if __name__ == '__main__':
    app.run(debug=True)

