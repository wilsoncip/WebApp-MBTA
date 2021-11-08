"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near, get_lat_long


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/station/", methods=["GET", "POST"])
def station():
    if request.method == "POST":
        place = request.form["location"]
        nearest_station = find_stop_near(place)

        if nearest_station:
            coordinates = get_lat_long(place)
            return render_template(
                "result.html",
                nearest_station = nearest_station['station_name'],
                wheelchair_accessible = nearest_station['wheelchair_accessible'],
                APIKEY = 'SzamCwiHRLf3Rlj4Nj5Qe4OzLuPsjS96VEhzAu06eU8'
            )
        else:
            return render_template("form.html", error=True)
    return render_template("form.html", error=None)



if __name__ == '__main__':
    app.run(debug=True)
