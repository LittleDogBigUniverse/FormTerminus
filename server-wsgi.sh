#!/usr/bin/env bash

echo
echo ===========================================================================
echo 'Starting prod server'
echo ===========================================================================
echo

cd webapp
gunicorn -b localhost:5000 -w 6 wsgi:app wsgi.py