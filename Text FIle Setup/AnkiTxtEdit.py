import os
import pandas as pd
import azure.cognitiveservices.speech as speechsdk
import PySimpleGUI as sg
import duplicates as dup
from pathlib import Path
subscription_key = "36141e3b7be442e3a09a06e8e93e4ae8"
region = "eastus"
CSVPath = Path('/Users/033103kennedymensah/Python_Automation_Projects/Text FIle Setup')
CSVPath.parent.mkdir(parents=True, exist_ok=True)


def text_to_speech(word, filename):
    speech_config = speechsdk.SpeechConfig(
        subscription=subscription_key, region=region)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    speech_config.speech_synthesis_voice_name = 'fr-FR-DeniseNeural'

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    synthesizer.speak_text_async(word).get()


def convert_words_to_mp3(word_list, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    sound_list = []
    for word in word_list:
        filename = f"{word}.mp3"
        text_to_speech(word, filename)
        sound_list.append(f"[sound:{filename}]")
    return sound_list


def remove_blank_lines(file):
    file = Path(file)
    lines = file.read_text().splitlines()
    filtered = [
        line
        for line in lines
        if line.strip()
    ]
    file.write_text('\n'.join(filtered))

def setup_for_anki(primary, secondary, output, media_path):
    output = str(output)
    remove_blank_lines(primary)
    remove_blank_lines(secondary)
    primary_list = open(primary).read().splitlines()
    secondary_list = open(primary).read().splitlines()
    for i in range(len(primary_list)):
        primary_list[i] = primary_list[i].replace('\t', ' ')
    for i in range(len(secondary_list)):
        secondary_list[i] = secondary_list[i].replace('\t', ' ')
    sound_list = convert_words_to_mp3(secondary_list, media_path)
    Full_Dict = {'Front': primary_list,
                 'Back': secondary_list, 'Audio': sound_list}
    Datalist = pd.DataFrame(Full_Dict)
    Datalist.to_csv(output)
    dupes = dup.list_all_duplicates(media_path, to_csv=True, csv_path='Text FIle Setup/dupe_list', ext='.jpg')


