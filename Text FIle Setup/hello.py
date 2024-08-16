import os
import pandas as pd
import azure.cognitiveservices.speech as speechsdk
import PySimpleGUI as sg
from pathlib import Path
import duplicates as dup
subscription_key = "14002341a5db4547ac38ad95492473b0"
region = "eastus"
French_words = "hello.txt"


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
        sound_list.append(f"[sound:{word}.mp3]")
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


remove_blank_lines(f"{French_words}")


french_list = open(
    f"{French_words}").read().splitlines()

for i in range(len(french_list)):
    french_list[i] = french_list[i].replace('\t', ' ')



convert_words_to_mp3(french_list, 'tester')
