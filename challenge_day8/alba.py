import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def extract_company_url():
    company_urls = []
    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text, "html.parser")
    company_list = soup.find(
        "div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all("li")
    for address in company_list:
        company_url = address.find('a')["href"]
        company_urls.append(company_url)
    return company_urls


def file_name(something):
    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text, "html.parser")
    nameofcompany = soup.find("div", {"id": "MainSuperBrand"}).find(
        "ul", {"class": "goodsBox"}).find("span", {"class": "company"}).text
    return nameofcompany


def extract_job(html):
    try:
        place = html.find("td", {"class": "local"}).text.replace("\xa0", " ")
    except:
        place = None
    try:
        title = html.find("span", {"class": "company"}).text
    except:
        title = None
    try:
        time = html.find("td", {"class": "data"}).find(
            "span", {"class": "time"}).text
    except:
        time = None
    try:
        pay = html.find("td", {"class": "pay"}).text
    except:
        pay = None
    try:
        date = html.find("td", {"class": "regDate"}).text
    except:
        date = None

    return {
        'place': place,
        'title': title,
        'time': time,
        'pay': pay,
        'date': date
    }


def extract_jobs(url):
    jobs = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("tbody").find_all("tr", {"class": ""})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def save_to_file(jobs):
    file = open(f"{name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


for company in extract_company_url()[:-3]:
    name = file_name(company)
    jobs = extract_jobs(company)
    save_to_file(jobs)
