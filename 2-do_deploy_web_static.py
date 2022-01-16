#!/usr/bin/python3
"""fabric file that deploys web static content to my servers"""
from fabric.api import run, put
import os

env.hosts = ["35.196.44.201", "18.208.171.12"]


def do_deploy(archive_path):
    """function that creates targz file out of web_static directory"""
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            filename = archive_path.split("/")[1]
            filename2 = filename.split(".")[0]
            name = "/data/web_static/releases/" + filename2 + "/"
            run("mkdir -p" + name)
            run("tar -xzf /tmp/" + filename + " -C " + name)
            run("rm /tmp/" + filename)
            run("mv " + name + "web_static/* " + name)
            run("rm -rf" + name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
    else:
        return False
