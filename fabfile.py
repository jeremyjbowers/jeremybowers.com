import json
import os

from fabric.api import *
import gspread


def get_wines():
  gc = gspread.login(os.environ.get('GMAIL_ACCOUNT'), os.environ.get('GMAIL_PASSWORD'))
  doc = gc.open("Cellar")
  sh = doc.get_worksheet(0)
  wines = sh.get_all_values()
  return [dict(zip(wines[0], w)) for w in wines[1:]]

def write_wine_json():
  wines = get_wines()

  with open("data/wine.json", "wb") as writefile:
    writefile.write(json.dumps(wines))
