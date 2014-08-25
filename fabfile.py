import glob
import json
import os

from fabric.api import local, require, settings, task
from fabric.operations import put
from fabric.state import env
from fabric.contrib.project import rsync_project
import gspread
from termcolor import colored

import app

env.user = "ubuntu"
env.forward_agent = True

env.hosts = "jeremybowers.com"
env.settings = None

@task
def get_wines():
  gc = gspread.login(os.environ.get("GMAIL_ACCOUNT"), os.environ.get("GMAIL_PASSWORD"))
  doc = gc.open("Cellar")
  sh = doc.get_worksheet(0)
  wines = sh.get_all_values()
  return [dict(zip(wines[0], w)) for w in wines[1:]]

@task
def write_wine_data():
  wines = get_wines()

  with open("www/wine/wine.json", "wb") as writefile:
    writefile.write(json.dumps(wines))

@task
def deploy():
  write_wine_data()
  rsync_project("/var/www/jeremybowers.com", "www/", delete=True)