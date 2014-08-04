import json
import os

from fabric.api import local, require, settings, task
from fabric.state import env
import gspread
from termcolor import colored

import app

def get_wines():
  gc = gspread.login(os.environ.get('GMAIL_ACCOUNT'), os.environ.get('GMAIL_PASSWORD'))
  doc = gc.open("Cellar")
  sh = doc.get_worksheet(0)
  wines = sh.get_all_values()
  return [dict(zip(wines[0], w)) for w in wines[1:]]

@task
def write_wine_json():
  wines = get_wines()

  with open("data/wine.json", "wb") as writefile:
    writefile.write(json.dumps(wines))

@task
def deploy_wine_data():
