# Readme.md
# Assumptions
1. The webcrawler will be used by a website, so developed a flask app wrapping the fetch(url) and getWebsiteAssets(urls) function
2. The images downloaded will be stored locally in disk, since its the way for now. Created an empty images folder where images from website will be downloaded 

# Flask webcrawler
Simple Flask webcrawler application which fetches href for <a> and src for <img>
After fetching the src of img and href of link tags from a webpage  

## Setup and run instructions
Install pipenv for virtualenv

    pip install pipenv
    pipenv shell
    pipenv update

which includes
* flask
* pytest
* Beautifulsoup4
* Requests

For Development environment, create a copy of .env.example file as below

    cp .env.example .env

Without the .env file, the app will run as production mode

To run the application,

    pipenv run python app.py

To run the unit test,

    pipenv run python -m pytest

To run the app in docker,


    docker build -t webcrawler .
    # to run in development mode
    docker run -it --rm -p 8080:8080 -e ENVIRONMENT=DEVELOPMENT -e PORT=8080 webcrawler
     # to run in production mode
    docker run -it --rm -p 80:80 webcrawler
