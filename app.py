"""Application entry point."""
import os, requests, sys
from flask import Flask, request, jsonify
from methods import getWebsiteAssets
from dotenv import *

load_dotenv()

app = Flask(__name__)

def handlers(app):

    @app.route('/')
    def getroute():
        return "Hello World", 200


    @app.route('/', methods=['POST'])
    def getImages():
        data = request.get_json()
        if data and data.get("url"):
            try:
                if getWebsiteAssets(data["url"]):
                    res = { "status": "201","message": "Images Downloaded"}
                    return jsonify(res), 201
            except Exception as e:
                res = { "status": "500", "message" : "{}".format(e) }
                return jsonify(res), 500

        else:
            res = { "status": "400", "message" : "Invalid Payload, Expecting parameter \'url\'" }
            return jsonify(res), 400


handlers(app)

if __name__ == "__main__":
    if os.getenv('ENVIRONMENT') == 'DEVELOPMENT':
        app.run(host='0.0.0.0',port=os.getenv('PORT'),debug=True)
    elif os.getenv('ENVIRONMENT') == 'PRODUCTION' or not os.getenv('ENVIRONMENT'):
        app.run(host='0.0.0.0',port='80')