from flask import Flask, request, render_template, abort
import requests
import re
from bs4 import BeautifulSoup
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/', methods=['GET'])
def count_words_from_url():
    url = request.args.get('url', 0, type=str)
    if url is 0:
        abort(400)
    response = requests.get(url)
    html_source = response.text  # html code from url
    soup = BeautifulSoup(html_source, 'html.parser')
    text_from_html = soup.get_text(" ").lower()  # text between html tags in lower case
    text_from_html = re.sub(r"[^a-zA-Z\']+", " ", text_from_html)  # remove special characters and numbers
    text_from_html = text_from_html.replace(" \'", " ").replace("\' ", " ")  # remove single quotes
    text_from_html = text_from_html.replace("we ve", "we\'ve")
    word_list = text_from_html.split(" ")
    del word_list[-1]  # remove last empty element
    """Form a dictionary of words and their numbers"""
    word_dict = {}
    for word in word_list:
        number = text_from_html.count(word)
        word_dict[word] = number
    """Convert the dictionary to an HTML table"""
    word_counter = ""
    for word, number in word_dict.items():
        word_counter += "<tr><td>" + word + ":</td><td>" + str(number) + "</td></tr>"

    word_counter = "<table border=0>" + word_counter + "</table>"
    return render_template(word_counter)

@app.errorhandler(Exception)
def handle_exception(e):
    # HTTP errors
    if isinstance(e, HTTPException):
        return "HTTP error"

    # non-HTTP errors
    return "Incorrect URL"

if __name__ == '__main__':
    app.run()
