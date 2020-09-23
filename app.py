"""Application entry point."""
import os
from flask import Flask, request, jsonify
from webcrawler import getWebsiteAssets
from dotenv import *

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['POST'])
def getImages():
    data = request.get_json()
    if getWebsiteAssets(data["url"]):
        return 201
    else:
        return 500

if __name__ == "__main__":
    if os.getenv('ENVIRONMENT') == 'DEVELOPMENT':
        app.run(host='0.0.0.0',port=os.getenv('PORT'),debug=True)
    elif os.getenv('ENVIRONMENT') == 'PRODUCTION' or not os.getenv('ENVIRONMENT'):
        app.run(host='0.0.0.0',port='80')