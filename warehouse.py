# -*- coding:utf-8 -*-

# 2021/10/06
import tkinter
import PySimpleGUI as sg
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

import pyperclip

# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI
# pip install pyperclip

#help(sg.Table)

config = Config()

t_03_星 = config.Base.classes.LifeLog_t_03_星

#Session = sessionmaker(bind=config.engine)
session = Session(config.engine)


def 過去ログ(data=None):
    session = Session(config.engine)
    print(data)
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    過去ログ = session.query(t_03_星).order_by(desc(t_03_星.日付)).limit(30)


    # ウィンドウの内容を定義する
    # 画面レイアウトを指定

    member_list = []

    print(過去ログ)
    for i in 過去ログ:
        #print(i)
        member_list.append([i.id, i.日付, i.間時間, i.大賢者の一言])
    session.close()
    return member_list

header = ["ID", "日付", "間時間", "大賢者の一言"]

def max_id():
    session = Session(config.engine)
    # 過去ログテーブル　の計算
    過去ログ = session.query(t_03_星).order_by(desc(t_03_星.開始時間)).limit(30)
    # 最大値の計算
    i = []
    for s in 過去ログ:
        i.append(s.id)
    session.close()
    return max(i) + 1


def やり方コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.やり方)
    session.close()
    return i

def おかず1コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.おかず1)
    session.close()
    return i

def おかず2コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.おかず2)
    session.close()
    return i

def おかず作者コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.おかず作者)
    session.close()
    return i

def シチュエーションコンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.シチュエーション)
    session.close()
    return i

def キャラクターの名前コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        print(s)
        i.append(s.キャラクターの名前)
    session.close()
    return i

def 大賢者の一言コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.大賢者の一言)
    session.close()
    return i

def T_206_Warez倉庫_idコンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.T_206_Warez倉庫_id)
    session.close()
    return i

def ファイル名コンボボックス():
    session = Session(config.engine)
    # コンボボックス = session.query(t_103_ライフログ).group_by(t_103_ライフログ.場所).all() # 動かない？
    コンボボックス = session.query(t_03_星).all()
    print(コンボボックス)
    i = []
    for s in コンボボックス:
        i.append(s.ファイル名)
    session.close()
    return i

id = max_id()

#T1 = sg.Column ([[sg.Listbox(プロジェクト(), enable_events=True, key="-プロジェクト-", size=(20, 20)), ]])

layout = sg.Column([
  [sg.Text('★管理')],
  [sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('日付', size=(10,1)), sg.CalendarButton('Choose Date', target=(1,0), key="-日付-", size=(20,1)), sg.Button(button_text='日付',key="日付")],
  [sg.Text('開始時間', size=(10,1)), sg.InputText('', key="-開始時間-", size=(20,1)), sg.Button(button_text='開始時間',key="開始時間")],
  [sg.Text('終了時間', size=(10,1)), sg.InputText('', key="-終了時間-", size=(20,1)), sg.Button(button_text='終了時間',key="終了時間")],
  [sg.Text('間時間', size=(10,1)), sg.InputText('', key="-間時間-", size=(20,1)), sg.Button(button_text='間時間',key="間時間"), sg.Button(button_text='保存',key="保存")],
  
  [sg.Text('やり方', size=(10,1)), sg.Combo(やり方コンボボックス(), size=(50, 5), key="-やり方-")],
  [sg.Text('おかず1', size=(10,1)), sg.Combo(おかず1コンボボックス(), size=(50, 5), key="-おかず1-")],
  [sg.Text('おかず2', size=(10,1)), sg.Combo(おかず2コンボボックス(), size=(50, 5), key="-おかず2-")],
  [sg.Text('おかず作者', size=(10,1)), sg.Combo(おかず作者コンボボックス(), size=(50, 5), key="-おかず作者-")],
  [sg.Text('シチュエーション', size=(10,1)), sg.Combo(シチュエーションコンボボックス(), size=(50, 5), key="-シチュエーション-")],
  [sg.Text('キャラクター', size=(10,1)), sg.Combo(キャラクターの名前コンボボックス(), size=(50, 5), key="-キャラクターの名前-")],
  [sg.Text('ページ', size=(10,1)), sg.InputText('', key="-ページ-", size=(50, 5))],
  [sg.Text('大賢者の一言', size=(10,1)), sg.Combo(大賢者の一言コンボボックス(), size=(50, 5), key="-大賢者の一言-")],

  [sg.Text('T_206_Warez倉庫_id', size=(10,1)), sg.Combo(T_206_Warez倉庫_idコンボボックス(), size=(50, 5), key="-T_206_Warez倉庫_id-")],
  [sg.Text('ファイル名', size=(10,1)), sg.Combo(ファイル名コンボボックス(), size=(50, 5), key="-ファイル名-"), sg.Button(button_text='クリップボード',key="クリップボード")],
   ])

T2 = sg.Column([[sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, key="過去ログ", size=(75, 10)), ]])

L=[
[sg.Pane([layout], orientation='h')],
[sg.Pane([T2], orientation='h')]
]

# ウィンドウを作成する
window = sg.Window('★管理', L, resizable=True)

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

        # 保存
        session = Session(config.engine)
        if session.query(t_03_星).filter(t_03_星.id == values["-ID-"]).first() == None:
            print("insert")

            session.add(t_03_星(id = max_id(),
                                        日付 = 日付,
                                        開始時間 = start_time,
                                        終了時間 = end_time,
                                        #間時間 = ma_time,
                                        やり方 = values["-やり方-"],
                                        おかず1 = values["-おかず1-"],
                                        おかず2 = values["-おかず2-"],
                                        おかず作者 = values["-おかず作者-"],
                                        シチュエーション = values["-シチュエーション-"],
                                        キャラクターの名前 = values["-キャラクターの名前-"],
                                        ページ = values["-ページ-"],
                                        大賢者の一言 = values["-大賢者の一言-"],
                                        T_206_Warez倉庫_id = values["-T_206_Warez倉庫_id-"],
                                        ファイル名 = values["-ファイル名-"],

            ))
        else:
            print("update")
            i = session.query(t_03_星).filter(id == values["-ID-"]).first()
            i.id = values["-ID-"],
            i.日付 = values["-日付-"],
            i.開始時間 = values["-開始時間-"],
            i.終了時間 = values["-終了時間-"],
            #i.間時間 = values["-間時間-"],
            i.やり方 = values["-やり方-"],
            i.おかず1 = values["-おかず1-"],
            i.おかず2 = values["-おかず2-"],
            i.おかず作者 = values["-おかず作者-"],
            i.シチュエーション = values["-シチュエーション-"],
            i.キャラクターの名前 = values["-キャラクターの名前-"],
            i.ページ = values["-ページ-"],
            i.大賢者の一言 = values["-大賢者の一言-"],
            i.T_206_Warez倉庫_id = values["-T_206_Warez倉庫_id-"],
            i.ファイル名 = values["-ファイル名-"],

        session.commit()
        values["-ID-"] = max_id()
        window["-大賢者の一言-"].update("保存完了")
        window["-過去ログ-"].update(過去ログ())
        session.close()
    
    elif event == "クリップボード":
        pyperclip.copy(f"* ★[★]:[Private]:\n{values['-やり方-']}\t{values['-おかず1-']}\t{values['-おかず2-']}\t{values['-おかず作者-']}\t{values['-シチュエーション-']}\t{values['-キャラクターの名前-']}\t{values['-ページ-']}\n{values['-大賢者の一言-']}\n")

    elif event == "-閉じる-":
        break
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()