#!/bin/bash
exec gunicorn --chdir app app:app -w 2 --threads 2 -b 0.0.0.0:80