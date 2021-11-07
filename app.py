"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/station/", methods=["GET", "POST"])
def station():
    if request.method == "POST":
        place = request.form["place"]
        nearest_station = find_stop_near(place)

        if nearest_station:
            return render_template(
                "result.html",
                place=place,
                nearest_station=nearest_station
            )
        # else:
    #         return render_template("form.html", error=True)
    # return render_template("form.html", error=None)



if __name__ == '__main__':
    app.run(debug=True)
