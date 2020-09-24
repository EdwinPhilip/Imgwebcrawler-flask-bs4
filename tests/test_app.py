import os,json
from flask import Flask, request, jsonify
from webcrawler.methods import getWebsiteAssets


from webcrawler.handlers.handlers import handlers


def test_base_route():
    app = Flask(__name__)
    handlers(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello World'
    assert response.status_code == 200

def test_post_route__success():
    app = Flask(__name__)
    handlers(app)
    client = app.test_client()
    url = '/'
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    mock_request_data = {
        "url": ["https://wowslider.com/web-photo-gallery-subway-basic.html"]
    }
    response = client.post(url, data=json.dumps(mock_request_data), headers=headers)
    assert response.status_code == 201

def test_post_route__failure_internal_server_error():
    app = Flask(__name__)
    handlers(app)
    client = app.test_client()
    url = '/'
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    mock_request_data = {
        "url": ["http://abc2311277s97.com"]
    }
    response = client.post(url, data=json.dumps(mock_request_data), headers=headers)
    assert response.status_code == 500


def test_post_route__failure__bad_request():
    app = Flask(__name__)
    handlers(app)
    client = app.test_client()
    url = '/'

    mock_request_data = {}
    expected = { "status": "400", "message" : "Invalid Payload, Expecting parameter \'url\'" }
    response = client.post(url, data=json.dumps(mock_request_data))
    assert response.get_json() == expected
    assert response.status_code == 400