#!/usr/bin/python3
# fabric file to create tgz file
from fabric.api import run, local
import os

os.environ.hosts = ["35.196.44.201", "18.208.171.12"]


def do_clean(number=0):
    if number >= 1:
        local("ls -1tr | head -n -1 | xargs rm -f versions")
        run("ls -1tr | head -n -1 | xargs rm -f /data/web_static/releases")
    else:
        local("ls -1tr | head -n -1 | xargs rm -f versions")
        run("ls -1tr | head -n -1 | xargs rm -f /data/web_static/releases")
