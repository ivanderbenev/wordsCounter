from flask import Flask
import requests
from html.parser import HTMLParser

app = Flask(__name__)

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        return data

@app.route('/')
def hello_world():  # put application's code here
    response = requests.get("https://www.bbc.co.uk/")
    parser = MyHTMLParser()
    parser.feed(response.text)
    return str(response.text)


if __name__ == '__main__':
    app.run()
