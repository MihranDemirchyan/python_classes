import random
import string
import requests
import pprint

# EX-1

def password_generator():
    while True:
        password = ""
        chars = string.ascii_letters + string.digits + string.punctuation

        for i in range(10):
            password += random.choice(chars)

        yield password


pass_gen = password_generator()
for line, pass_ in enumerate(range(5), start=1):
    print(f"{line} | {next(pass_gen)}")


# EX-2

url = "https://zenquotes.io/api/random"

def quotes_generator():
    while True:
        try:
            responce_ = requests.get(url)
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("Internet connection lost")

        if responce_.status_code == 200:
            data = responce_.json()
            yield data


quotes = quotes_generator()
for i in range(2):
    pprint.pprint(next(quotes))