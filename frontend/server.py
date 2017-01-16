import csv

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    houses = []
    with open('houses.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            houses.append({
                'id': row['id'],
                'price': row['price'],
                'surface': row['surface'],
            })
    return render_template('index.html', houses=houses)


if __name__ == '__main__':
    app.run(debug=True)
