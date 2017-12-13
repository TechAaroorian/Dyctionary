#!/usr/bin/env python3


import subprocess
import time
import os


def main():
    startjulius = os.path.join(
        os.getcwd(),
        "/SpeechRecognition-Julius/Dy_Open.sh")

    startwindow = subprocess.Popen(
        ['python3', 'Dy_StartupWindow.py'],
        shell=False)

    subprocess.Popen(['sh', startjulius], shell=False)
    subprocess.Popen(['python3', 'DyctionaryUI.py'], shell=False)

    time.sleep(18)
    startwindow.kill()


if __name__ == '__main__':
    main()
