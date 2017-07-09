#!/usr/bin/env python3
import subprocess, time, os

julius_start = os.getcwd() + "/SpeechRecognition-Julius/Dy_Open.sh"

startUP = subprocess.Popen(['python3', 'Dy_StartupWindow.py'], shell=False)

subprocess.Popen(['sh', julius_start], shell=False)

Dyctionary = subprocess.Popen(['python3', 'DyctionaryUI.py'], shell=False)

time.sleep(18)

startUP.kill()
#os.system("exit")