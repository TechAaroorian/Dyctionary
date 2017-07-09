#!/bin/sh
cd SpeechRecognition-Julius
padsp julius -C Dy_SpeechReg.jconf | python3 Dy_SpeechReg.py
