from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    response = requests.get("https://www.bbc.co.uk/")
    return str(response.text)


if __name__ == '__main__':
    app.run()
