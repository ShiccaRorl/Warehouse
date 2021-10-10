# -*- encoding: utf-8 -*-

import configparser

import datetime

from sqlalchemy import * 
from sqlalchemy.orm import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# pip install psycopg2

# ファイルの存在チェック用モジュール
import os
import errno


class Config:
    def __init__(self):


        # --------------------------------------------------
        # read_file()関数によるiniファイルの読み込み
        # --------------------------------------------------
        config_ini = configparser.ConfigParser()
        config_ini_path = './config.ini'

        # iniファイルが存在するかチェック
        if os.path.exists(config_ini_path):
            # iniファイルが存在する場合、ファイルを読み込む
            with open(config_ini_path, encoding='utf-8') as fp:
        
                config_ini.read_file(fp)

                read_default = config_ini['DEFAULT']

                self.driver = read_default.get('driver')
                self.username = read_default.get('username')
                self.password = read_default.get('password')
                self.host = read_default.get('host')
                self.port = read_default.get('port')
                self.database = read_default.get('database')
                # self.db_path_access1 = self.db_path_access1.replace('"', '')

        else:
            print("iniファイルがない")

        self.Base = automap_base()
        # postgresql://scott:tiger@localhost/mydatabase
        
        # 接続文字列
        self.engine = create_engine(f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}')
        
        #self.Base = declarative_base(bind=self.engine)
        self.Base.prepare(self.engine, reflect=True)


if __name__ == '__main__':
    config = Config()
