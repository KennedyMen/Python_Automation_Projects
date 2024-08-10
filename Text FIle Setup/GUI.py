import PySimpleGUI as sg  # pip install pysimplegui
import os
from os.path import isfile, join
from os import listdir
import pandas as pd
import azure.cognitiveservices.speech as speechsdk
import PySimpleGUI as sg
from pathlib import Path
from AnkiTxtEdit import *

# -------------GUI Layout-----------------#
Layout = [
         [sg.Text("Primary Language File:"), sg.Input(key="-LANGUE-"),
          sg.FileBrowse(file_types=(("Plain text", "*.txt"),))],
         [sg.Text("Secondary Language File:"),
          sg.Input(key="-2meLANGUE-"), sg.FileBrowse(file_types=(("Plain text", "*.txt"),))],
         [sg.Text("Output Folder:"), sg.Input(
             key="-OUTFOLD-"), sg.FolderBrowse()],
         [sg.Text("Path to collection.media:"), sg.Input(
             key="-MEDIA-"), sg.FolderBrowse()],
         [sg.Exit(), sg.Button("Setup for Anki"), sg.Text("Azure API KEY:"), sg.Input(key="-API-", size=(31, 4)),
          sg.Text("Azure Region:"), sg.Input(key="-REGION-", size=(15, 4))],
]

window = sg.Window("Anki Language Setup", Layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Setup for Anki":
        setup_for_anki(primary=values["-LANGUE-"], secondary=values["-2meLANGUE-"], output=values["-OUTFOLD-"],
                       media_path=values["-MEDIA-"], API=values["-API-"], REGION=values["-REGION-"])

window.close()
