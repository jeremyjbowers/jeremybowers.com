#!/usr/bin/env python

import json
import os
from sets import Set

import argparse
from flask import Flask, render_template, jsonify
import gspread

app = Flask(__name__)

@app.route('/api/v1/')
def api_controller():
  with open("data/wine.json", "r") as readfile:
    wines = json.loads(readfile.read())

  # for wine in wines:
  #   try:
  #     wine['cost'] = int(wine['cost'].replace('$', ''))
  #   except TypeError:
  #     wine['cost'] = None
  #   try:
  #     wine['size'] = int(wine['size'].replace('ml', ''))
  #   except TypeError:
  #     wine['size'] = None
  #   try:
  #     wine['year'] = int(wine['year'])
  #   except:
  #     wine['year'] = str(wine['year'])

  payload = {}
  count = 0
  payload['wines'] = []

  from flask import request

  for wine in wines:
    votes = 0
    for arg in dict(request.args).items():
      k = arg[0]
      v = arg[1][-1]
      if wine.get(k, None):
        if wine.get(k, None) == v or not v:
          votes += 1
    if len(dict(request.args).items()) == votes:
      payload['wines'].append(wine)


  payload['count'] = len(payload['wines'])
  return json.dumps(payload)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=True)