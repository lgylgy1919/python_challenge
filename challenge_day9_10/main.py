import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")

new_result = requests.get(new)
new_text = new_result.text

popular_result = requests.get(popular)
popular_text = popular_result.text


def get_popular_page():
    new_dict = []

    for section in lists


@app.route("/")
def homePage():
    return render_template("template/index.html")


@app.route("/?order_by=new")
def newPage():
    oId = new_dict["objectID"]
    titles = new_dict["title"]
    urls = new_dict["url"]
    points = new_dict["points"]
    authors = new_dict["author"]
    numbers = new_dict["num_comments"]
    return render_template(
        "template/index.html",
        objecetID=oId
        title=titles,
        url=urls,
        point=points,
        author=authors,
        num_comments=numbers

    )


@app.route("/?order_by=popular")
def popularPage():
    return render_template("template/index.html",
                           )


@app.route("/<id>")
def dd():
    return render_template("template/detail.html")


app.run(host="0.0.0.0")
