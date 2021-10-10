#!/bin/sh

#rm *

git pull

pkg install python

pip install -U pip

pip install pysimplegui
pkg install python-tkinter
pip install remi
pip install pysimpleguiweb

pip install configparser
pip install sqlalchemy
pip install psycopg2
pip install pyperclip

pip install -U configparser
pip install -U sqlalchemy
pip install -U psycopg2
pip install -U pyperclip

python warehouse.py

#pip install opencv-python
#pip install opencv-python

python camera.py