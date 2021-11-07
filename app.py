"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request

from mbta_helper import find_stop_near


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
            return render_template(
                "result.html",
                nearest_station = nearest_station['station_name'],
                wheelchair_accessible = nearest_station['wheelchair_accessible']
            )
        else:
            return render_template("form.html", error=True)
    return render_template("form.html", error=None)



if __name__ == '__main__':
    app.run(debug=True)
