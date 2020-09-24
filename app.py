"""Application entry point."""
import os, requests, sys
from flask import Flask, request, jsonify
from handlers.handlers import handlers
from dotenv import *

load_dotenv()

app = Flask(__name__)



handlers(app)

if __name__ == "__main__":
    if os.getenv('ENVIRONMENT') == 'DEVELOPMENT':
        app.run(host='0.0.0.0',port=os.getenv('PORT'),debug=True)
    elif os.getenv('ENVIRONMENT') == 'PRODUCTION' or not os.getenv('ENVIRONMENT'):
        app.run(host='0.0.0.0',port='80')