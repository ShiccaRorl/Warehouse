import PySimpleGUI as sg
import datetime

"""
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import * 
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
"""

from config import Config, Timebox
# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI
from peewee import *
from LifeLog_models import *


#help(sg.Table)

config = Config()

#t_07_読書 = config.Base.classes.LifeLog_t_07_読書

#Session = sessionmaker(bind=config.engine)
#session = Session(config.engine)

def 過去ログ(data=None):
    print(data)
    # 過去ログテーブル　の計算
    #session = Session(config.engine)
    #過去ログ = session.query(t_07_読書).order_by(desc(t_07_読書.日付)).limit(30)
    過去ログ = LifeLogT07読書.select().order_by(LifeLogT07読書.日付)
    # ウィンドウの内容を定義する
    # 画面レイアウトを指定


    member_list = []

    #print(t)
    for i in 過去ログ:
        member_list.append([i.id, i.タイトル, i.開始時間, i.終了時間, i.コメント])
    return member_list

header = ['ID', 'タイトル', '開始時間', '終了時間', "コメント"]

def 本タイトル():
    # コンボボックス　本タイトルの計算
    #t_07_本 = config.Base.classes.LifeLog_t_07_本
    #過去タイトル = session.query(t_07_本).filter(t_07_本.やりかけ == True).order_by(desc(t_07_本.日付)).all()
    過去タイトル = LifeLogT07本.select().where(LifeLogT07本.やりかけ==True).order_by(LifeLogT07本.日付)
    i = []
    for s in 過去タイトル:
        i.append(s.タイトル)
    過去タイトル = i
    return 過去タイトル

def 本ファイル名():
    # コンボボックス　本ファイル名の計算
    #t_206_warez倉庫 = config.Base.classes.LifeLog_t_206_warez倉庫
    #過去ファイル名 = session.query(t_206_warez倉庫).filter(t_206_warez倉庫.やりかけ == True).order_by(desc(t_206_warez倉庫.閲覧日)).all()
    過去ファイル名 = LifeLogT206Warez倉庫.select().where(LifeLogT206Warez倉庫.やりかけ==True).order_by(LifeLogT206Warez倉庫.閲覧日)
    i = []
    for s in 過去ファイル名:
        i.append(s.ファイル名)
    過去ファイル名 = i
    return 過去ファイル名

def max_id():
    # 過去ログテーブル　の計算
    #過去ログ = session.query(t_07_読書).order_by(desc(t_07_読書.日付)).limit(30)
    過去ログ = LifeLogT07読書.select().order_by(LifeLogT07読書.日付).limit(30)
    # 最大値の計算
    i = []
    for s in 過去ログ:
        i.append(s.id)
    return max(i) + 1

def 保存():
    print("insert")

    print("update")

def list更新():
    print("update")

def 読了():
    print("update")

def コピー():
    print("update")

id = max_id()


layout = [
  [sg.Text('読書時間管理')],
  [sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('開始時間', size=(10,1)), sg.InputText('', key="-開始時間-", size=(20,1)), sg.Button(button_text='開始時間',key="開始時間")],
  [sg.Text('終了時間', size=(10,1)), sg.InputText('', key="-終了時間-", size=(20,1)), sg.Button(button_text='終了時間',key="終了時間")],
  [sg.Text('間時間', size=(10,1)), sg.InputText('', key="-間時間-", size=(20,1)), sg.Button(button_text='間時間',key="間時間")],
  
  # コンボボックス
  [sg.Text('タイトル', size=(10, 1)), sg.Listbox(本タイトル(), enable_events=True, key="-タイトル-", size=(50, 5)), 
  sg.Text('ファイル名', size=(10,1)), sg.Listbox(本ファイル名(), enable_events=True, key="-ファイル名-", size=(50, 5))],
  
  [sg.Text('ページ', size=(10,1)), sg.InputText(default_text="", key="-ページ-")],
  [sg.Text('気付き1', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き1-")],
  [sg.Text('気付き2', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き2-")],
  [sg.Text('気付き3', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き3-")],
  [sg.Text('コメント', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-"), sg.Button(button_text='保存', key="-保存-"), sg.Button(button_text='読了', key="-読了-"), sg.Button(button_text="コピー", key="-コピー-"), sg.Button(button_text='閉じる', key="-閉じる-")],
  [sg.Text('過去ログ', size=(10,1)), sg.Table(過去ログ(), headings=header, size=(200, 10), key='-過去ログ-'), sg.Button(button_text='読み込み', key="-読み込み-")],
  ]

# ウィンドウを作成する
window = sg.Window('読書時間管理', layout, resizable=True)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "閉じるb":
        break
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
        window["-過去ログ-"].update("list")
    elif event == "-保存-":
        try:
            """
            session = Session(config.engine)
            if session.query(t_07_読書).filter(t_07_読書.id == values["-ID-"]).order_by(desc(t_07_読書.日付)).first() == None:
                session.query(t_07_読書).insert(id = values["-ID-"],
                                            開始時間 = values["-開始時間-"],
                                            終了時間 = values["-終了時間-"],
                                            間時間 = values["-間時間_input-"],
                                            タイトル = values["-タイトル-"],
                                            ファイル名 = values["-ファイル名-"],
                                            ページ = values["-ページ-"],
                                            気付き1 = values["-気付き1-"],
                                            気付き2 = values["-気付き2-"],
                                            気付き3 = values["-気付き3-"],
                                            コメント = values["-コメントt-"],
                )
            else:
                session.query(t_07_読書).update(id = values["-ID-"],
                                            開始時間 = values["-開始時間-"],
                                            終了時間 = values["-終了時間-"],
                                            間時間 = values["-間時間-"],
                                            タイトル = values["-タイトル-"],
                                            ファイル名 = values["-ファイル名-"],
                                            ページ = values["-ページ-"],
                                            気付き1 = values["-気付き1-"],
                                            気付き2 = values["-気付き2-"],
                                            気付き3 = values["-気付き3-"],
                                            コメント = values["-コメント-"],
                )
            """
        except:
            sg.PopupError('！エラー発生！')
    elif event == "-読了-":
        window["-読了-"].update("読了")
    elif event == "-閉じる-":
        break
    elif event == "-コピー-":
        window["-ID-"].update(max_id())
        window["-タイトル_id-"].update(values["-タイトル-"])
        window["-ファイル名_id-"].update("-ファイル名-")

    elif event == "-読み込み-":
        window["-読み込み-"].update("-読み込み-")
    """
    elif event == "リストボックス":
        #print(values[リストボックス])
        window["過去ログ"].update(過去ログ(values[リストボックス]))
    """
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()