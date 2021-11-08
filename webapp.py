"""
Flask application for MBTA information. Given location as input, returns nearest MBTA station as output. 
"""
from flask import Flask, render_template, request
from mbta_helper import find_stop_near
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        place = str(request.form["place"]) # refers to the "place" button in index.html
        station = find_stop_near(place)
        print(station)
        if station:
            return render_template("result.html", place = place, station = station)
        else: 
            return render_template("error.html", error=True)
    return render_template("index.html", error=None)



if __name__ =="__main__":
    app.run(debug=True)