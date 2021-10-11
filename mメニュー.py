# -*- coding:utf-8 -*-

# 2021/10/06

import PySimpleGUI as sg
import datetime


layout = [
  [sg.Text('メニュー管理')],
  [sg.Button(button_text='基本',key="基本"), sg.Button(button_text='睡眠',key="睡眠")],
  [sg.Button(button_text='アニメ',key="アニメ"), sg.Button(button_text='18禁アニメ',key="18禁アニメ")],
  [sg.Button(button_text='プログラム',key="プログラム"), sg.Button(button_text='検索文字列',key="検索文字列")],
  [sg.Button(button_text='映画',key="映画")],
  [sg.Button(button_text='読書',key="読書"), sg.Button(button_text='本',key="本"), sg.Button(button_text='★',key="★")],
  [sg.Button(button_text='コミック',key="コミック"), sg.Button(button_text='成年コミック',key="成年コミック"), sg.Button(button_text='同人',key="同人")],
  [sg.Button(button_text='Warez',key="Warez"), sg.Button(button_text='Warez倉庫',key="Warez倉庫")],
  [sg.Button(button_text='ゲーム',key="ゲーム"), sg.Button(button_text='18禁ゲーム',key="18禁ゲーム")],
  [sg.Button(button_text='プロジェクト',key="プロジェクト"), sg.Button(button_text='やりたい事リスト',key="やりたい事リスト")],
  [sg.Button(button_text='メニューログ',key="メニューログ")],
  ]

# ウィンドウを作成する
window = sg.Window('メニュー管理', layout, resizable=True)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "-閉じる-":
        break
    elif event == "基本":
        subprocess.Popen(["python", "./k基本.py"])
    elif event == "睡眠":
        subprocess.Popen(["python", "./s睡眠.py"])
    elif event == "アニメ":
        window["-開始時間-"].update(datetime.datetime.now())

    elif event == "18禁アニメ":
        window["-終了時間-"].update(datetime.datetime.now())

    elif event == "プログラム":
        window["-間時間-"].update(datetime.datetime.now())

    elif event == "検索文字列":
        #検索文字列menu_log = Menu_Log()
        #検索文字列menu_log.プログラム名("検索文字列")
        #検索文字列menu_log.start_time()
        subprocess.Popen(["python", "./k検索文字列.py"])
        #検索文字列menu_log.end_time()
        #検索文字列menu_log.保存()
    elif event == "映画":
        print("listが押された")

    elif event == "読書":
        subprocess.Popen(["python", "./t読書.py"])
        
    elif event == "本":
        print("")
    elif event == "★":
        subprocess.Popen(["python", "./h★.py"])

    elif event == "コミック":
        print("")

    elif event == "成年コミック":
        print("")

    elif event == "同人":
        print("")

    elif event == "ゲーム":
        print("")

    elif event == "18禁ゲーム":
        print("")

    elif event == "Warez":
        subprocess.Popen(["python", "./warez.py"])

    elif event == "Warez倉庫":
        subprocess.Popen(["python", "./warez倉庫.py"])

    elif event == "メニューログ":
        print("")

    elif event == "-閉じる-":
        break
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()