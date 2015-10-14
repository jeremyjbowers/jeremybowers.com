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
  with open("www/wine/wine.json", "r") as readfile:
    wines = json.loads(readfile.read())

  payload = []
  for wine in wines:
    if wine['consumed']:
        if wine['wine_type'] == "White":
            payload.append(1)
        elif wine['wine_type'] == "Orange":
            payload.append(-1)
        else:
            payload.append(0)

  return json.dumps(payload)

  # for wine in wines:
  #   try:
  #     wine['cost'] = float(wine['cost'].replace('$', ''))
  #   except TypeError:
  #     wine['cost'] = None
  # #   try:
  # #     wine['size'] = int(wine['size'].replace('ml', ''))
  # #   except TypeError:
  # #     wine['size'] = None
  #   try:
  #     wine['year'] = int(wine['year'])
  #   except:
  #     wine['year'] = str(wine['year'])

  # payload = {}
  # count = 0
  # payload['wines'] = []

  # from flask import request

  # for wine in wines:
  #   votes = 0

  #   if len(dict(request.args).items()) == 0:
  #     payload['wines'].append(wine)

  #   else:
  #     for arg in dict(request.args).items():
  #       k = arg[0]
  #       v = arg[1][-1]

  #     if "__" in k:
  #       k, comparator = k.split("__")

  #       try:
  #         v = int(v)
  #       except ValueError:
  #         pass

  #       if comparator == "lte":
  #         if wine.get(k, None):
  #           if isinstance(v, int) and isinstance(wine.get(k, None), int):
  #             if wine.get(k, None) <= v:
  #               votes += 1
  #             print votes

  #       if comparator == "gte":
  #         if wine.get(k, None):
  #           if isinstance(v, int) and isinstance(wine.get(k, None), int):
  #             if wine.get(k, None) >= v:
  #               votes += 1
  #             print votes

  #       if comparator == "lt":
  #         if wine.get(k, None):
  #           if isinstance(v, int) and isinstance(wine.get(k, None), int):
  #             if wine.get(k, None) < v:
  #               votes += 1
  #             print votes

  #       if comparator == "gt":
  #         if wine.get(k, None):
  #           if isinstance(v, int) and isinstance(wine.get(k, None), int):
  #             if wine.get(k, None) > v:
  #               votes += 1
  #             print votes

  #       if comparator == "in":
  #         if wine.get(k, None):
  #           if isinstance(v, str):
  #             if v in wine.get(k, None) or not v:
  #               votes +=1

  #       if comparator == "not":
  #         if wine.get(k, None):
  #           if isinstance(v, str):
  #             if v not in wine.get(k, None) or not v:
  #               votes += 1

  #       if comparator == "exact":
  #         if wine.get(k, None):
  #           if wine.get(k, None) == v or not v:
  #             votes += 1

  #       else:
  #         if wine.get(k, None):
  #           if wine.get(k, None) == v or not v:
  #             votes += 1

  #     if len(dict(request.args).items()) == votes:
  #       payload['wines'].append(wine)

  # payload['count'] = len(payload['wines'])
  # return json.dumps(payload)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=True)