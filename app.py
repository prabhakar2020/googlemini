from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import Flask, make_response, request
import json
import sqlite3 as sq


# A very simple Flask Hello World app for you to get started with...

from flask import Flask, make_response, request
import json
import sqlite3 as sq

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/webhook',methods=['POST'])
def webhook():
    if request.method == 'POST':
        req = request.get_json(silent = True, force = True)
        queryResult = req.get('queryResult')
        print ("+"*100)
        print (queryResult)
        parameters = queryResult.get('parameters','')
        speech = 'Hey '+str(name)+", glad to meet you"
        print (speech)

        response = {
            'fulfillmentText': speech
        }
        
        
        res = json.dumps(response, intent = 4)
        r = make_response(res)
        r.headers["Content-Type"] = "application/json"
        return r



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    app.run(debug=False, port=port, host='0.0.0.0')
