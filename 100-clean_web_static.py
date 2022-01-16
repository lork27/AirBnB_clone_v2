#!/usr/bin/python3
# fabric file to create tgz file
from fabric.api import run, local
import os

os.environ.hosts = ["35.196.44.201", "18.208.171.12"]


def do_clean(number=0):
    """cleans up local machine and server from old files"""
    delnum = number + 1
    if number == 0 or number == 1:
        local("cd versions; ls -1tr | tail -n +2 | xargs rm -rf")
        run("cd /data/web_static/releases; ls -1tr | tail -n +2 | xargs rm -rf")
    else:
        local("cd versions; ls -1tr | tail -n +{} | xargs rm -rf".format(delnum))
        run("cd /data/web_static/releases; ls -1tr | tail +{} | xargs rm -rf".format(delnum))
