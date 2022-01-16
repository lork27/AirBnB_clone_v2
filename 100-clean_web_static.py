#!/usr/bin/python3
# fabric file to create tgz file
from fabric.api import run
from datetime import datetime
import os

os.environ.hosts = ["35.196.44.201", "18.208.171.12"]


def do_clean(number=0):
    if number >= 1:
        run("ls -1tr | head -n -1 | rm -f versions")
        run("ls -1tr | head -n -1 | rm -f /data/web_static/releases")
    else:
        run("ls -1tr | head -n -2 | rm -f versions")
        run("ls -1tr | head -n -2 | rm -f /data/web_static/releases")
