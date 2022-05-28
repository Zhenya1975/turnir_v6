#!/bin/bash
rm fights.db
rm -r migrations
flask db init
flask db migrate -m 'init'
flask db upgrade
python fill_fighters.py