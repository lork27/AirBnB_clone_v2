#!/usr/bin/python3
"""fabric file that deploys web static content to my servers"""
from fabric.api import run, put
import os

os.environ.hosts = ["35.196.44.201", "18.208.171.12"]


def do_deploy(archive_path):
    """function that creates targz file out of web_static directory"""
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
    else:
        return False
