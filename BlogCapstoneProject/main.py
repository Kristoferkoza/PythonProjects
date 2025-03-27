import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Enter your name: "

@app.route('/<your_name>')
def guess(your_name):
    agify_link = requests.get(f"https://api.agify.io?name={your_name}").json()
    age = agify_link["age"]
    genderize_link = requests.get(f"https://api.genderize.io?name={your_name}").json()
    gender = genderize_link["gender"]


    return render_template("index.html", name=your_name, age=age, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)