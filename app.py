from flask import Flask
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    response = requests.get("https://www.bbc.co.uk/")
    html_source = response.text
    soup = BeautifulSoup(html_source, 'html.parser')
    return soup.get_text()


if __name__ == '__main__':
    app.run()
