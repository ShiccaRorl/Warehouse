import PySimpleGUIWeb as g

layout = [[g.T('This is my first window')],
          [g.In()],
          [g.T('', key='_OUT_')],
          [g.OK(), g.Cancel()]]

win = g.Window('My first Android Window', web_port=8080).Layout(layout)

while True:
    e,v = win.Read()
    print(e,v)
    if e in (None, 'Cancel'):
        break
    win.Element('_OUT_').Update(v[0])
win.Close()