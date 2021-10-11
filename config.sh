#!/bin/sh

#rm *

git pull

apt update
apt upgrade

pkg install python

pip install -U pip

pip install pysimplegui
pkg install python-tkinter
pip install remi
pip install pysimpleguiweb
pip install pysimplegui

pip install configparser
#pip install sqlalchemy
#pip install psycopg2
pip install pyperclip
pip install peewee

pip install -U configparser
#pip install -U sqlalchemy
#pip install -U psycopg2
pip install -U pyperclip
pip install -U peewee

python warehouse.py

#pip install opencv-python
#pip install opencv-python

python camera.py

pip install gnucash-portfolio-webui
runapp.sh
