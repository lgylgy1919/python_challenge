import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "https://www.iban.com/currency-codes"
countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code = items[2].text
    if name and code:
        if name != "No universal currency":
            country = {
                'name': name.capitalize(),
                'code': code
            }
            countries.append(country)


def ask_c1():
    try:
        choice = int(input("#: "))
        if choice > len(countries):
            print("choose a number from the list.")
            ask_c1()
        else:
            country_1 = countries[choice]
            print(country_1['name'])
    except ValueError:
        print("That wasn't a number.")
        ask_c1()

    def ask_c2():
        print("Now choose another country")
        try:
            choice = int(input("#: "))
            if choice > len(countries):
                print("choose a number from the list.")
                ask_c2()
            else:
                country_2 = countries[choice]
                print(country_2['name'])
        except ValueError:
            print("That wasn't a number.")
            ask_c2()
        print(
            f"How many {country_1['code']} do you want to convert to {country_2['code']}?")

        def trans():
            try:
                money = format(int(input()),',')
                url_trans = f"https://transferwise.com/gb/currency-converter/{country_1['code']}-to-{country_2['code']}-rate?amount={money}"
                request = requests.get(url_trans)
                soup = BeautifulSoup(request.text, "html.parser")
                value = soup.find(
                    "input", {"class": "js-TargetAmount"})["value"]
                print(
                    f"{country_1['code']} {money} is {country_2['code']} {value}")
            except:
                print("That wasn't a number")
                trans()

        trans()
    ask_c2()


print("Welcome to Currency Convert PRO 2020")
for index, country in enumerate(countries):
    print(f"#{index} {country['name']}")


print("Where are you from? Choose a country by number")
ask_c1()
