#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os, sys

#Importamos " SpeechRecognition".
import speech_recognition as sr

#Definimos archivo de audio.
audio = "cancionRapcortada.wav"

#Iniciamos reconocedor de voz.
re = sr.Recognizer()

#Conversión Audio-Texto
with sr.AudioFile(audio) as source:
    #Obtención de información del audio.
    info_audio = re.record(source)
    #Conversión a texto.
    texto = re.recognize_google(info_audio, language = "es-ES")
    #Imprimimos texto
    print(texto)