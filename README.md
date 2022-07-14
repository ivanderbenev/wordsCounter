# wordsCounter manual
A web service that receives a URL of a website and returns the number of word occurrences of text held with the html tags.
## URL-based API
The service is accessed by attaching the desirable web address as a URL argument after the '?', for example: /?url=https://www.bbc.co.uk/
The out put is a table of words and numbers of their occurences.
## Dependendencies
All the dependencies are listed in the file requirements.txt
## Docker
To build a docker image please use the command in the directory containing app.py:
$ docker build -t wordcounter-docker . 
To run the docker container with the app pleas euse the following command:
$ docker run -d -p 5000:5000 wordcounter-docker
The app should be running on http://localhost:5000/
