#!/bin/sh

python ../restaurant/manage.py makemigrations
python ../restaurant/manage.py migrate
python ../restaurant/manage.py loaddata initial_data.json