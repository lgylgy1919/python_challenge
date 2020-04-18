import requests
from bs4 import BeautifulSoup

print("Hello! Please choose select a country by number:")
URL = "https://www.iban.com/currency-codes"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")

name_one = soup.find("tbody")
name_two = name_one.find_all("td")

list = []
for link in name_two:
    list.append(link.string)

country_list = list[0::4]
code_list = list[2::4]


for index, country_name in enumerate(country_list, 1):
    print("#{} {}" .format(index, country_name))


def ask():
    print("#: ", end="")
    try:
        number = int(input())
        if 1 <= number <= 268:
            print(
                f"You choose {country_list[number-1]}\nThe currency code is {code_list[number-1]}")
        else:
            print("Choose a number from the list.")
            ask()
    except:
        print("That wasn't a number")
        ask()


ask()
