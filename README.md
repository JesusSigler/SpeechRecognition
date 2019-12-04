# SpeechRecognition

Script realizado en Python que utiliza la librería de Google "Speech Recognition" para convertir el audio en texto plano y mostrándolo por pantalla.

Sistema Operativo: Linux Ubuntu con entorno de escritorio LXDE.

Para el testeo se ha utilizado un fragmento de la canción "Mi consejo" de Rafa Espino, la aplicación no soporta videos largos por lo que se ha utilizado solo unos segundos del audio.

Paraconseguir el audio se ha extraído el audio del videoclip del artista utilizando la aplicación online https://www.onlinevideoconverter.com/es y una vez descargado el audio se ha recortado la pista de audio a un tamaño el cual la aplicación pueda soportarla, para ello se ha tenido que hacer varias pruebas ya que se pretendía que la aplicación mostrara un texto considerable por pantalla.

Problemas que han surgido durante el testeo:

1 - No se encontraba el módulo llamado speech_recognition
2 - Problemas de Encoding
3- Interrupción de la aplicación debido a la longitud del audio


Soluciones

1- Instalación del módulo
2- adición de un encoding, para ello se ha utilizado de fuente la página https://www.python.org/dev/peps/pep-0263/, la cual fue       indicada por consola en el momento que ocurrió el problema, además ya que el idioma del audio es en español se tuvo que mantener el parámetro language = "es-ES" del método recognize_google().
3- Se redujo el tamaño del audio a convertir, para ello se tuvo que realziar varias pruebas de ensallo y error.

Este código fue extraído de la siguiente fuente:

https://programacionpython80889555.wordpress.com/2019/12/03/obteniendo-texto-de-un-archivo-de-audio-en-python-con-speechrecognition/?fbclid=IwAR0zNb3O-mv2kdEqW1SWiVRqoNb0v5NztSLFPBTR-5D5iiUU5zbh_jkDGtU

La finalidad de este test fue únicamente por pura curiosidad sobre el funcionamiento de esta librería.
