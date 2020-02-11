from flask import Flask, render_template, jsonify, request
from feeders import (
    hackernews, devto, techcrunch, reddit,
    producthunt, freecodecamp, hackernoon
    )

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def feed():
    if request.method == "GET":
        return render_template("feed.html")
    else:
        service = request.json
        print(service)
        if service["feed"] == "dev":
            data = devto.get_articles()
            return jsonify(data)
        elif service["feed"] == "hackernews":
            data = hackernews.get_top()
            return jsonify(data)
        elif service["feed"] == "techcrunch":
            data = techcrunch.feed()
            print(data)
            return jsonify(data)
        elif service["feed"] == "reddit":
            print(service)
            data = reddit.subreddit(service["sub"], service["sort"])
            return jsonify(data)
        elif service["feed"] == "producthunt":
            data = producthunt.feed()
            print(data)
            return jsonify(data)
        elif service["feed"] == "freecodecamp":
            data = freecodecamp.feed()
            print(data)
            return jsonify(data)
        elif service["feed"] == "hackernoon":
            data = hackernoon.feed()
            print(data)
            return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)