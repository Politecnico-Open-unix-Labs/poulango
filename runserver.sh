#! /bin/sh

uwsgi --socket /path/to/something.sock --plugin python --wsgi-file poulango/wsgi.py
