import os
import pandas as pd
import azure.cognitiveservices.speech as speechsdk
from pathlib import Path
subscription_key = "36141e3b7be442e3a09a06e8e93e4ae8"
region = "eastus"


def text_to_speech(word, filename):
    speech_config = speechsdk.SpeechConfig(
        subscription=subscription_key, region=region)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    speech_config.speech_synthesis_voice_name ='fr-FR-DeniseNeural'

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    synthesizer.speak_text_async(word).get()


def convert_words_to_mp3(word_list, output_dir="Text FIle Setup/media"):
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


remove_blank_lines("Text FIle Setup/Phrases en anglasi.txt")
remove_blank_lines("Text FIle Setup/Phrases en Francais .txt")


english_list = open(
    "Text FIle Setup/Phrases en anglasi.txt").read().splitlines()
french_list = open(
    "Text FIle Setup/Phrases en Francais .txt").read().splitlines()

for i in range(len(english_list)):
    english_list[i] = english_list[i].replace('\t', ' ')
for i in range(len(french_list)):
    french_list[i] = french_list[i].replace('\t', ' ')


mediafilist = convert_words_to_mp3(french_list, output_dir="Text FIle Setup/media")