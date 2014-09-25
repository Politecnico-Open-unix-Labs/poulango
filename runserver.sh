#! /bin/sh

uwsgi --socket /tmp/poul_manifesti.sock --plugin python --wsgi-file poulango/wsgi.py


