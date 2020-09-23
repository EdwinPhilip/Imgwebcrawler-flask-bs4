"""Application entry point."""
from flask import Flask
from webcrawler import getWebsiteAssets

app = Flask(__name__)


@app.route('/')
def getImages():

    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)