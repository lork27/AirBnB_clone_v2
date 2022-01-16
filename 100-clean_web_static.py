#!/usr/bin/python3
# fabric file to create tgz file
from fabric.api import run, local
import os

os.environ.hosts = ["35.196.44.201", "18.208.171.12"]


def do_clean(number=0):
    """cleans up local machine and server from old files"""
    delnum = number + 1
    if number <= 1:
        local("ls -1tr | head -n -1 | xargs rm -rf versions")
        run("ls -1tr | head -n -1 | xargs rm -rf /data/web_static/releases")
    else:
        local("ls -1tr | head -n -{} | xargs rm -rf versions".format(delnum))
        run("ls -1tr | head -n -{} | xargs rm -rf /data/web_static/releases".format(delnum))
