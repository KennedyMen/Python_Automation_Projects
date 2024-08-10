import PySimpleGUI as sg #pip install pysimplegui
import os
import pandas as pd
import azure.cognitiveservices.speech as speechsdk
import PySimpleGUI as sg
from pathlib import Path
subscription_key = "36141e3b7be442e3a09a06e8e93e4ae8"
region = "eastus"
CSVPath = Path('/Users/033103kennedymensah/Python_Automation_Projects/Text FIle Setup')
CSVPath.parent.mkdir(parents=True, exist_ok=True)

#-------------GUI Layout-----------------#
Layout = [
         [sg.Text("Primary Language File:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("text","*.txt*"),))],
         [sg.Text("Secondary Language File:"), sg.Input(key="-IN-"), sg.FileBrowse()],
         [sg.Text("Azure API Key:"), sg.Input(key="-IN-"), sg.FileBrowse()],
         [sg.Text("Azure Region:"), sg.Input(key="-IN-"), sg.FileBrowse()],
         [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
         [sg.Text("Path to collection.media:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
         [sg.Exit(), sg.Button("Setup for Anki")],
]

window = sg.Window("Anki Language Setup", Layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert to CSV":
        sg.popup_error("Not yet implemented")
window.close()