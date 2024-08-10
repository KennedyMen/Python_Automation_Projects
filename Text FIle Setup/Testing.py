import pandas as pd
import os
from pathlib import Path
import PySimpleGUI as sg
CSVPath = Path(
    '/Users/033103kennedymensah/Python_Automation_Projects/Text FIle Setup')
CSVPath.parent.mkdir(parents=True, exist_ok=True)

hello = ['hi', 'hello', 'jojo', 'its']
likely = ['jf', 'kil', 'likes', 'idk']
man = ['kel', 'hello', 'animal', 'all']

dict = {'English': hello, 'French': likely, 'Audio': man}

Datalist = pd.DataFrame(dict)
print(Datalist)
Datalist.to_csv(
    '/Users/033103kennedymensah/Python_Automation_Projects/Text FIle Setup/Study.csv', encoding='utf-8')

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
