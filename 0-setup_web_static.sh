#!/usr/bin/env bash
#Script that installs and setup nginx web server and its structure
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test
chown -R ubuntu:ubuntu /data
service nginx restart
