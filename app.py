# app.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

app.run(
    port=int(os.getenv('PORT', 8086)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

if __name__ == '__main__':
    app.run(debug=True)