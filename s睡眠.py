# -*- coding:utf-8 -*-

# 2021/10/06

import PySimpleGUIWeb as sg
import datetime

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import * 
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
import webbrowser
import subprocess

# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI


#help(sg.Table)

config = Config()

t_02_睡眠 = config.Base.classes.LifeLog_t_02_睡眠

#Session = sessionmaker(bind=config.engine)
session = Session(config.engine)


def 過去ログ(data=None):
    session = Session(config.engine)
    print(data)
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    過去ログ = session.query(t_02_睡眠).order_by(desc(t_02_睡眠.日付)).limit(30)


    # ウィンドウの内容を定義する
    # 画面レイアウトを指定

    member_list = []

    print(過去ログ)
    for i in 過去ログ:
        #print(i)
        member_list.append([i.id, i.日付, i.間時間, i.コメント])
    session.close()
    return member_list

header = ["ID", "日付", "間時間", "コメント"]

def max_id():
    session = Session(config.engine)
    # 過去ログテーブル　の計算
    過去ログ = session.query(t_02_睡眠).order_by(desc(t_02_睡眠.開始時間)).limit(30)
    # 最大値の計算
    i = []
    for s in 過去ログ:
        i.append(s.id)
    session.close()
    return max(i) + 1


def コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_02_睡眠).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.場所)
    session.close()
    return i


id = max_id()

#T1 = sg.Column ([[sg.Listbox(プロジェクト(), enable_events=True, key="-プロジェクト-", size=(20, 20)), ]])

layout = sg.Column([
  [sg.Text('睡眠管理')],
  [sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('日付', size=(10,1)), sg.InputText('', key="-日付-", size=(20,1)), sg.Button(button_text='日付',key="日付")],
  [sg.Text('開始時間', size=(10,1)), sg.InputText('', key="-開始時間-", size=(20,1)), sg.Button(button_text='開始時間',key="開始時間")],
  [sg.Text('終了時間', size=(10,1)), sg.InputText('', key="-終了時間-", size=(20,1)), sg.Button(button_text='終了時間',key="終了時間")],
  [sg.Text('間時間', size=(10,1)), sg.InputText('', key="-間時間-", size=(20,1)), sg.Button(button_text='間時間',key="間時間"), sg.Button(button_text='保存',key="保存")],
  
  [sg.Text('場所', size=(10,1)), sg.Combo(コンボボックス(), size=(50, 5), key="-場所-")],

  [sg.Text('コメント', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-")],
   ])

T2 = sg.Column([[sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, key="過去ログ", size=(75, 10)), ]])

L=[[sg.Pane([layout], orientation='h')],
    [sg.Pane([T2], orientation='h')]]

# ウィンドウを作成する
window = sg.Window('睡眠管理', L, resizable=True)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "-閉じる-":
        break
    elif event == "日付":
        window["-日付-"].update(datetime.date.today())
        日付 = datetime.date.today()
    elif event == "開始時間":
        window["-開始時間-"].update(datetime.datetime.now())
        start_time = datetime.datetime.now()
    elif event == "終了時間":
        window["-終了時間-"].update(datetime.datetime.now())
        end_time = datetime.datetime.now()
    elif event == "間時間":
        window["-間時間-"].update(end_time - start_time)
        ma_time = end_time - start_time

    elif event == "-過去ログ-":
        print("listが押された")
        d = 0
        moji = ""
        data = values["-過去ログ-"]
        for org in data:
            for i in org:
                if d == 1:
                    print(i)
                    moji = i
                d = d + 1
        # print(data[1])
        window["-検索文字列-"].update(moji)
        window["-過去ログ-"].update(過去ログ())

    elif event == "保存":
        # コマンド
        try:
            # 保存
            session = Session(config.engine)
            if session.query(t_02_睡眠).filter(t_02_睡眠.id == values["-ID-"]).first() == None:
                print("insert")

                session.add(t_02_睡眠(id = max_id(),
                                        日付 = 日付,
                                        開始時間 = start_time,
                                        終了時間 = end_time,
                                        #間時間 = ma_time,
                                        場所 = values["-場所-"],
                                        コメント = values["-コメント-"],
                ))
            else:
                print("update")
                i = session.query(t_02_睡眠).filter(id == values["-ID-"]).first()
                i.id = values["-ID-"],
                i.日付 = values["-日付-"],
                i.開始時間 = values["-開始時間-"],
                i.終了時間 = values["-終了時間-"],
                #i.間時間 = values["-間時間-"],
                i.場所 = values["-場所-"],
                i.コメント = values["-コメント-"],

            session.commit()
            id = max_id()
            window["-コメント-"].update("保存完了")
            window["-過去ログ-"].update(過去ログ())
            session.close()
        except:
            sg.PopupError('！エラー発生！')
    elif event == "-閉じる-":
        break
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()