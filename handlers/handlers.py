"""Handlers for Scrape img and link attributes from a requested Page URL."""
import os, requests, sys
from flask import Flask, request, jsonify
from methods import getWebsiteAssets
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
