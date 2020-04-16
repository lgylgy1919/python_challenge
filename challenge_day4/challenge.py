import requests
import os


def boilerplate():
    print("welcome to IsItDown")
    print("Please write a URL or URLs you want to check (seperated by comma)")
    address = input()
    add_arr = address.split(',')
    for item in add_arr:
        clean_add = item.strip().lower()

        if clean_add.endswith("com") or clean_add.endswith("net"):
            if clean_add.startswith("http://"):
                try:
                    result = requests.get(clean_add)
                    code = result.status_code
                    if code == 200:
                        print(f"{clean_add} is up!")
                    elif code == 203:
                        print(f"{clean_add} is down!")
                except:
                    print(f"{clean_add} is down!")

            else:
                full_add = "http://" + clean_add
                try:
                    result = requests.get(full_add)
                    code = result.status_code
                    if code == 200:
                        print(f"{full_add} is up!")
                    elif code == 203:
                        pritn(f"{full_add} is down!")
                except:
                    print(f"{full_add} is down!")

        else:
            print(f"{clean_add} is not a valid url")

    def restart():
        print("Do you want to start over? y/n")
        answer = input()
        if answer == "y" or answer == "n":
            if answer == "n":
                print("Ok, bye")
                return
            else:
                def clear(): return os.system('cls')
                clear()
                boilerplate()
        else:
            print(f"{answer} is not a valid answer")
            restart()

    restart()


boilerplate()
