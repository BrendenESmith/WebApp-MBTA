"""
Flask application for MBTA information. Given location as input, returns nearest MBTA station as output. 
"""
from flask import Flask, render_template, request
from mbta_helper import get_json, find_stop_near
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        address = str(request.form["address"])
        information = get_json(address)
        if information:
            return find_stop_near(render_template("result.html"),
            station = information
            )
        else: 
            return render_template("index.html", error=True)
    return render_template("index.html", error=None)



if __name__ =="__main__":
    app.run(debug=True)