from flask import Flask, render_template
import os
import csv
PEOPLE_FOLDER = os.path.join('static','images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
content = []
ylist = []
whaty = 0


# Reading CSV File
def readb(year):
    with open('static/Years/' + year + '.csv', 'r') as g:
        csv_reader = csv.DictReader(g)
        for line in csv_reader:
            content.append(line)


# Getting a the list of csv files and taking the .csv off for ease of readability
def listyears():
    arr = os.listdir('static/Years')
    for line in arr:
        back = line[len(line)::-1]
        fixed = back[4:len(back)]
        forward = fixed[len(fixed)::-1]
        ylist.append(forward)


# Home Page
listyears()
@app.route('/')
def home():
    return render_template("home.html", years=ylist, on=whaty)


# Converting whaty into a file name
year = ylist[whaty]
readb(str(year))

# Year Page
@app.route('/year')
def year():
    return render_template("year.html", content=content)


if __name__ == '__main__':
    app.run(debug=True)
