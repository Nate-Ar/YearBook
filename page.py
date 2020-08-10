from flask import Flask, render_template
import os
import csv
import time
PEOPLE_FOLDER = os.path.join('static','images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
content = []


def readb():
    with open('static/2020.csv', 'r') as g:
        csv_reader = csv.DictReader(g)
        for line in csv_reader:
            content.append(line)


readb()
@app.route('/')
def home():
    return render_template("home.html", content=content)


if __name__ == '__main__':
    app.run(debug=True)
