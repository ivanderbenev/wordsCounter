from flask import Flask
import requests
from bs4 import BeautifulSoup
import re
import json

app = Flask(__name__)


@app.route('/')
def count_words_from_url():
    word_dict = {}
    response = requests.get("https://www.bbc.co.uk/")
    html_source = response.text  # html code from url
    soup = BeautifulSoup(html_source, 'html.parser')
    text_from_html = soup.get_text(" ").lower()  # text between html tags in lower case
    text_from_html = re.sub(r"[^a-zA-Z\']+", " ", text_from_html)  # remove special characters and numbers
    text_from_html = text_from_html.replace(" \'", " ").replace("\' ", " ")  # remove single quotes
    text_from_html = text_from_html.replace("we ve", "we\'ve")
    word_list = text_from_html.split(" ")
    del word_list[-1]  # remove last empty element
    for word in word_list:
        number = text_from_html.count(word)
        word_dict[word] = number

    word_counter = ""
    for word, number in word_dict.items():
        word_counter += "<tr><td>" + word + ":</td><td>" + str(number) + "</td></tr>"

    word_counter = "<table border=0>" + word_counter + "</table>"
    return word_counter


if __name__ == '__main__':
    app.run()
