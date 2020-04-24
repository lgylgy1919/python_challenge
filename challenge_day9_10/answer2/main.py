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

def get_items(url):
  data = requests.get(url).json()
  return data
  

@app.route("/")
def home():
  if request.args.get("order_by"):
    orderBy=request.args.get("order_by")
  else:
    orderBy = "popular"
  if orderBy == "popular":
    url = popular
  else:
    url = new
  existingData = db.get(orderBy)
  if existingData:
    data = existingData
  else:
    data = get_items(url)["hits"]
    db[orderBy] = data  
  return render_template("index.html",orderBy=orderBy, posts=data)

@app.route("/<int:id>")
def details(id): 
  url = make_detail_url(id)
  data = get_items(url)
  comments = data["children"]
  return render_template("detail.html", data=data, comments = comments)


app.run(host="0.0.0.0")