# Dyctionary main file for User Interface
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from uiinit import UserInterfaceInit
import subprocess, os, threading, time
import Dyctionary_Modules.DyctionaryCSS as DyctionaryCSS
import Dyctionary_Modules.Dy_UserEntryAnalyzer as Dy_UserEntryAnalyzer


class Dy_UserInterface(UserInterfaceInit):
    def __init__(self, ):
        UserInterfaceInit.__init__(self)

        self.Dy_UserEntryAnalyzerObject = Dy_UserEntryAnalyzer.Dy_UserEntryAnalyzer()

        self.Dy_MainCss = DyctionaryCSS.DyctionaryCSS
        self.Dy_StyleProvider = Gtk.CssProvider()
        self.Dy_StyleProvider.load_from_data(self.Dy_MainCss)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), self.Dy_StyleProvider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # self.add(self.Dy_ScrollWindow)
        self.add(self.Dy_VBoxTwo)

        self.Dy_MakeIntroThread = threading.Thread(target=self.Dy_MakeIntro)
        self.Dy_MakeIntroThread.start()

        self.meeted = False

    def Dy_MakeIntro(self):
        time.sleep(2.8)
        subprocess.Popen(['espeak', '-v', 'f5', 'welcome'], shell=False)

    def Dy_ListenFunction(self, Dy_Listen):
        if self.Dy_ListenStart:
            self.Dy_ListenStart = False
            self.Dy_ListenButtonI.set_from_file(self.Dy_IconDir +
                                                "Listen_Icon_Red_35.png")
            self.Dy_Spinner.start()
            self.Dy_SpinnerSpeak.stop()
            self.Dy_StatusBottomOne.set_label(self.Dy_StatusBottomOneText[1])

            self.Dy_SpeechRegThread = threading.Thread(
                target=self.Dy_SpeechReg)
            self.Dy_SpeechRegThread.start()

    def Dy_SpeechReg(self, ):
        self.Dy_UserQueryText = "SpeechRecognition has been activated. I Need your permission to continue. Are you ready?"
        self.Dy_UserQuery.set_label(self.Dy_UserQueryText)
        time.sleep(2.5)
        subprocess.Popen(
            ['espeak', '-s', '120', '-v', 'f5', 'Are your ready?'],
            shell=False)

        while True:
            self.Dy_SpeechRegFile = open(
                self.Dy_SpeechRegPath + "Dy_SpeechReg.output", 'r')
            self.Dy_SpeechRegInput = str(self.Dy_SpeechRegFile.readline())

            if self.Dy_SpeechRegInput == "READY LETS START " and self.Dy_ListenReady == False:
                self.Dy_StatusBottomTwo.set_label(
                    self.Dy_StatusBottomTwoText[1])
                self.Dy_StatusBottomThree.set_label(
                    self.Dy_StatusBottomThreeText[1])
                self.Dy_UserQueryText = "Cool.. what do you thinking?"
                subprocess.Popen(
                    ['espeak', '-s', '140', '-v', 'f3', 'Speak something'],
                    shell=False)
                self.Dy_UserQuery.set_label(self.Dy_UserQueryText)
                time.sleep(5)
                self.Dy_ListenReady = True
                continue

            if self.Dy_ListenReady:
                if self.Dy_SpeechRegInput == 'THIS IS COMMAND STOP LISTENING ':
                    self.Dy_SpeechRegFile.close()
                    self.Dy_ListenButtonI.set_from_file(
                        self.Dy_IconDir + "Listen_Icon_35.png")
                    self.Dy_Spinner.stop()
                    self.Dy_SpinnerSpeak.start()
                    self.Dy_ListenReady = False
                    self.Dy_ListenStart = True
                    self.Dy_StatusBottomOne.set_label(
                        self.Dy_StatusBottomOneText[2])
                    self.Dy_StatusBottomTwo.set_label(
                        self.Dy_StatusBottomTwoText[0])
                    self.Dy_StatusBottomThree.set_label(
                        self.Dy_StatusBottomThreeText[0])
                    subprocess.Popen(
                        ['espeak', 'Listening have stopped'], shell=False)
                    break
                elif self.Dy_SpeechRegInput == 'READY LETS START ':
                    pass
                else:
                    try:
                        self.fixResult = []
                        if self.Dy_SpeechRegInputPre != self.Dy_SpeechRegInput:
                            self.fixResult, check = self.Dy_UserEntryAnalyzerObject.Dy_Evaluation(
                                self.Dy_SpeechRegInput.lower())
                            self.Dy_fixEverThing(self.fixResult, check)
                    except Exception as e:
                        pass

                    self.Dy_SpeechRegFile.close()
                    self.Dy_SpeechRegInputPre = self.Dy_SpeechRegInput
                    time.sleep(1)

    def Dy_SpeakLoud(self, Dy_SpeakLoud, Dy_SpeakType):
        try:
            if Dy_SpeakType == 'S':
                subprocess.Popen([
                    'espeak', '-s', '160', '-v', 'f5',
                    self.Dy_ResponseSmallSpeech
                ])

            if Dy_SpeakType == 'M':
                subprocess.Popen([
                    'espeak', '-s', '145', '-v', 'f5',
                    self.Dy_ResponseLargeSpeech
                ])
        except:
            subprocess.Popen(
                ['espeak', '-v', 'f5', '-s', '145', 'Unable to Read..'])

        self.set_focus(self.Dy_UserEntry)

    def Dy_TextEntry(self, Dy_UserEntry):

        Dy_TextEntryData = self.Dy_UserEntry.get_text()
        Dy_FinalLongTextResponse = self.Dy_UserEntryAnalyzerObject.Dy_ResponseInstant(
            Dy_TextEntryData.strip())
        self.Dy_UserQuery.set_label(Dy_FinalLongTextResponse)

    def Dy_TextEntryFinal(self, Dy_UserEntry):
        checkExist = None
        self.Dy_UserEntryAnalyzerObject = Dy_UserEntryAnalyzer.Dy_UserEntryAnalyzer(
        )
        Dy_TextEntryData = self.Dy_UserEntry.get_text()
        self.fixResult, checkExist = self.Dy_UserEntryAnalyzerObject.Dy_Evaluation(
            Dy_TextEntryData)

        self.Dy_fixEverThing(self.fixResult, checkExist)
        #self.Dy_MainImage.set_from_file(self.Dy_IconDir + "Sm1.png")

    def Dy_fixEverThing(self, fixList, checkExist):

        if len(fixList) == 1:
            print("yes")
            self.Dy_UserQueryText = fixList[0]

            self.Dy_UserQuery.set_label(self.Dy_UserQueryText)
            self.set_focus(self.Dy_UserEntry)
            self.Dy_MainImage.set_from_file(self.Dy_IconDir + "Sm1.png")
        else:
            self.Dy_ResponseLargeText = fixList[0]
            self.Dy_ResponseSmallText = fixList[1]
            self.Dy_ResponseLargeSpeech = fixList[2]
            self.Dy_UserQueryText = fixList[3]
            self.Dy_ResponseSmallSpeech = fixList[3]

            self.Dy_ResponseLarge.set_markup(self.Dy_ResponseLargeText)
            self.Dy_ResponseSmall.set_label(self.Dy_ResponseSmallText)
            self.Dy_UserQuery.set_label(self.Dy_UserQueryText)

            subprocess.Popen(
                ['espeak', '-v', 'f5', self.Dy_ResponseSmallSpeech])
            self.set_focus(self.Dy_UserEntry)

    def Dy_callMoreWindow(self, moreWindow):
        if self.meeted:
            self.Dy_additionalWindow.kill()
        try:
            self.Dy_additionalWindow = subprocess.Popen(
                [
                    'python3',
                    'Dy_additionalWindow.py',
                    self.Dy_ResponseSmallSpeech,
                    self.fixResult[5],
                    self.fixResult[4],
                    self.fixResult[6],
                ],
                shell=False)
            self.meeted = True
        except:
            subprocess.Popen(
                ['espeak', '-v', 'f5', 'your last search not supported'],
                shell=False)

    def Dy_CloseAll(self, Dy_SwitchOff):
        self.Dy_Spinner.stop()
        self.Dy_SpinnerSpeak.stop()
        self.Dy_ListenReady = True
        self.Dy_SpeechRegStop = open(
            self.Dy_SpeechRegPath + "Dy_SpeechReg.output", 'w')
        self.Dy_SpeechRegStop.write("THIS IS COMMAND STOP LISTENING ")
        self.Dy_SpeechRegStop.close()
        os.system("killall julius")
        if self.meeted:
            self.Dy_additionalWindow.kill()
        Gtk.main_quit()


def main():
    DyUI = Dy_UserInterface()
    DyUI.connect("delete-event", Gtk.main_quit)
    DyUI.maximize()
    DyUI.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
