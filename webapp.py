"""
Flask application for MBTA information. Given location as input, returns nearest MBTA station as output. 
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



if __name__ =="__main__":
    app.run(debug=True)