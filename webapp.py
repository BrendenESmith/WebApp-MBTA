"""
Flask application for MBTA information. Given location as input, returns nearest MBTA station as output. 
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", method=["GET","POST"])
def index():
    if request.method == "POST":
        address = float(request.form["address"])
    return render_template("index.html")



if __name__ =="__main__":
    app.run(debug=True)