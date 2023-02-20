#!/bin/sh

mkdir -p media
cd media
umask 000
cd ..

pipenv run gunicorn -b 0.0.0.0:8000 senne.wsgi
