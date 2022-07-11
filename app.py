from flask import Flask
import urllib3

http = urllib3.PoolManager()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    response = http.request("GET", "https://www.bbc.co.uk", verify=False)
    return response.status


if __name__ == '__main__':
    app.run()
