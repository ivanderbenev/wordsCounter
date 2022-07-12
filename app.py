from flask import Flask
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)


@app.route('/')
def count_words_from_url():
    response = requests.get("https://www.bbc.co.uk/")
    html_source = response.text  # html code from url
    soup = BeautifulSoup(html_source, 'html.parser')
    text_from_html = soup.get_text(" ")  # text between html tags
    text_from_html = re.sub(r"[^a-zA-Z\']+", " ", text_from_html)  # remove special characters and numbers
    text_from_html = text_from_html.replace(" \'", " ").replace("\' ", " ")  # remove single quotes
    text_from_html = text_from_html.replace("we ve", "we\'ve")
    # f = open("text_from_html.txt", "w")
    # f.write(text_from_html)
    # f.close
    return text_from_html


if __name__ == '__main__':
    app.run()
