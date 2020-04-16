import requests

indeed_result = requests.get(
    "https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8&limit=50&radius=25")

print(indeed_result.text)
