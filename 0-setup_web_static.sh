#!/usr/bin/env bash
#Script that installs and setup nginx web server and its structure
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hola muy buenas!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test
chown -R ubuntu:ubuntu /data
sed -i '\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
