import csv
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
    wines = []
    with open('www/wine/wine.csv', 'r') as readfile:
        reader = csv.DictReader(readfile)
        return [dict(r) for r in reader]

@task
def write_wine_data():
  wines = get_wines()

  with open("www/wine/wine.json", "wb") as writefile:
    writefile.write(json.dumps(wines))

@task
def deploy():
  write_wine_data()
  rsync_project("/var/www/jeremybowers.com", "www/", delete=True)
