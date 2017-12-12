#!/usr/bin/env python3
from Dyctionary_Modules.Dy_WordNetAccess import wordnetAccess
from gi.repository import Gtk, Gdk
import os, subprocess
import time


class Dy_UserInterfaceInit(Gtk.Window):
    def __init__(self, ):
        Gtk.Window.__init__(self, title="Dyctionary")

        fixdataInit = []
        check = None

        self.checkStatisfied = True

        while self.checkStatisfied:
            try:
                self.wrdntObject = wordnetAccess()
                fixdataInit, check = self.wrdntObject.randomWordInit()
                self.fixResult = fixdataInit
                self.checkStatisfied = False

                if fixdataInit[3] == "No Source Found":
                    self.checkStatisfied = True
            except Exception as e:
                print(e)

        self.Dy_ListenStart = True
        self.Dy_ListenReady = False
        self.Dy_SpeechRegInputPre = ""

        # status initialization
        self.Dy_StatusBottomOneText = [
            "SpeechRecognition not activated yet",
            "SpeechRecognition activated", "SpeechRecognition has deactivated"
        ]
        self.Dy_StatusBottomTwoText = ["Sleeping", "Listening"]
        self.Dy_StatusBottomThreeText = [
            "Normal Mode", "Listening Mode", "Dictionary Mode"
        ]

        self.Dy_UserQueryText = fixdataInit[3]
        self.Dy_ResponseLargeText = fixdataInit[0]
        self.Dy_ResponseSmallText = fixdataInit[1]
        self.Dy_ResponseLargeSpeech = fixdataInit[2]
        self.Dy_ResponseSmallSpeech = fixdataInit[3]
        self.Dy_IconDir = os.getcwd() + "/Icons/"
        self.Dy_SpeechRegPath = os.getcwd() + "/SpeechRecognition-Julius/"

        self.set_icon_from_file(self.Dy_IconDir + "DyLogo.png")
        self.set_default_size(1024, 720)
        self.set_size_request(400, 400)
        self.set_border_width(10)
        self.set_name("Dy_MainWindow")

        self.Dy_ScrollWindow = Gtk.ScrolledWindow()
        self.Dy_ScrollWindow.set_policy(Gtk.PolicyType.ALWAYS,
                                        Gtk.PolicyType.ALWAYS)

        self.Dy_HBoxOne = Gtk.HBox(spacing=6)
        self.Dy_HBoxTwo = Gtk.HBox(spacing=12)
        self.Dy_VBoxOne = Gtk.VBox(spacing=12)
        self.Dy_HButtonBoxOne = Gtk.HButtonBox(spacing=6)
        self.Dy_VBoxTwo = Gtk.VBox(spacing=0)
        self.Dy_HBoxThree = Gtk.HButtonBox()

        self.Dy_TopLabelDummy = Gtk.Label()

        self.Dy_UserQuery = Gtk.Label()
        self.Dy_UserQuery.set_label(self.Dy_UserQueryText)
        self.Dy_UserQuery.set_justify(Gtk.Justification.FILL)
        self.Dy_UserQuery.set_line_wrap(True)
        self.Dy_UserQuery.set_size_request(640, 20)
        self.Dy_UserQuery.set_name("Dy_UserQuery")

        self.Dy_ResponseLarge = Gtk.Label()
        self.Dy_ResponseLarge.set_markup(self.Dy_ResponseLargeText)
        self.Dy_ResponseLarge.set_justify(Gtk.Justification.FILL)
        self.Dy_ResponseLarge.set_selectable(True)
        self.Dy_ResponseLarge.set_line_wrap(True)
        self.Dy_ResponseLarge.set_max_width_chars(115)
        self.Dy_ResponseLarge.set_size_request(640, 480)
        self.Dy_ResponseLarge.set_name("Dy_ResponseLarge")

        self.Dy_MainWindowTitle = Gtk.Label()
        self.Dy_MainWindowTitle.set_label("Dyctionary")
        self.Dy_MainWindowTitle.set_name("Dy_MainWindowTitle")

        self.Dy_ResponseSmall = Gtk.Label()
        self.Dy_ResponseSmall.set_label(self.Dy_ResponseSmallText)
        self.Dy_ResponseSmall.set_justify(Gtk.Justification.FILL)
        self.Dy_ResponseSmall.set_line_wrap(True)
        self.Dy_ResponseSmall.set_max_width_chars(25)
        self.Dy_ResponseSmall.set_size_request(300, 100)
        self.Dy_ResponseSmall.set_name("Dy_ResponseSmall")

        self.Dy_MainImage = Gtk.Image()
        self.Dy_MainImage.set_from_file(self.Dy_IconDir + "Sm1.png")
        self.Dy_MainImage.set_size_request(300, 300)
        self.Dy_MainImage.set_tooltip_text("Visual")
        self.Dy_MainImage.set_name("Dy_MainImage")

        self.Dy_UserEntry = Gtk.Entry()
        self.Dy_UserEntry.set_size_request(640, 30)
        self.Dy_UserEntry.set_inner_border(None)
        self.Dy_UserEntry.connect("changed", self.Dy_TextEntry)
        self.Dy_UserEntry.connect("activate", self.Dy_TextEntryFinal)
        self.Dy_UserEntry.set_name("Dy_UserEntry")

        self.Dy_DummyStart = Gtk.Label()
        self.Dy_DummyEnd = Gtk.Label()

        self.Dy_SwitchOffButton = Gtk.Button()
        self.Dy_SwitchOffButton.set_name("Dy_Buttons")
        self.Dy_SwitchOffButton.set_relief(2)
        self.Dy_SwitchOffButtonI = Gtk.Image()
        self.Dy_SwitchOffButtonI.set_from_file(self.Dy_IconDir +
                                               "Switch_off_35.png")
        self.Dy_SwitchOffButton.set_image(self.Dy_SwitchOffButtonI)
        self.Dy_SwitchOffButton.connect("clicked", self.Dy_CloseAll)
        self.Dy_SwitchOffButton.set_tooltip_text("Close Dyctionary")
        self.Dy_SwitchOffButton.set_size_request(20, 20)

        self.Dy_ListenButton = Gtk.Button()
        self.Dy_ListenButton.set_name("Dy_Buttons")
        self.Dy_ListenButton.set_relief(2)
        self.Dy_ListenButtonI = Gtk.Image()
        self.Dy_ListenButtonI.set_from_file(self.Dy_IconDir +
                                            "Listen_Icon_35.png")
        self.Dy_ListenButton.set_image(self.Dy_ListenButtonI)
        self.Dy_ListenButton.connect("clicked", self.Dy_ListenFunction)
        self.Dy_ListenButton.set_tooltip_text("Activate Microphone")
        self.Dy_ListenButton.set_size_request(35, 35)

        self.Dy_SearchButton = Gtk.Button()
        self.Dy_SearchButton.set_name("Dy_Buttons")
        self.Dy_SearchButton.set_relief(2)
        self.Dy_SearchButtonI = Gtk.Image()
        self.Dy_SearchButtonI.set_from_file(self.Dy_IconDir +
                                            "Search_Icon_35.png")
        self.Dy_SearchButton.set_image(self.Dy_SearchButtonI)
        self.Dy_SearchButton.connect("clicked", self.Dy_TextEntryFinal)
        self.Dy_SearchButton.set_tooltip_text("Find")
        self.Dy_SearchButton.set_size_request(35, 35)

        self.Dy_MoreButton = Gtk.Button()
        self.Dy_MoreButton.set_name("Dy_Buttons")
        self.Dy_MoreButton.set_relief(2)
        self.Dy_MoreButtonI = Gtk.Image()
        self.Dy_MoreButtonI.set_from_file(self.Dy_IconDir + "More_Icon_35.png")
        self.Dy_MoreButton.set_image(self.Dy_MoreButtonI)
        self.Dy_MoreButton.connect("clicked", self.Dy_callMoreWindow)
        self.Dy_MoreButton.set_tooltip_text("More")
        self.Dy_MoreButton.set_size_request(35, 35)

        self.Dy_SpeakLButton = Gtk.Button()
        self.Dy_SpeakLButton.set_name("Dy_Buttons")
        self.Dy_SpeakLButton.set_relief(2)
        self.Dy_SpeakLButtonI = Gtk.Image()
        self.Dy_SpeakLButtonI.set_from_file(self.Dy_IconDir +
                                            "Speak_Icon_35.png")
        self.Dy_SpeakLButton.set_image(self.Dy_SpeakLButtonI)
        self.Dy_SpeakLButton.set_tooltip_text("Speak Main")
        self.Dy_SpeakLButton.set_size_request(35, 35)
        self.Dy_SpeakLButton.connect("clicked", self.Dy_SpeakLoud, 'M')

        self.Dy_SpeakMButton = Gtk.Button()
        self.Dy_SpeakMButton.set_name("Dy_Buttons")
        self.Dy_SpeakMButton.set_relief(2)
        self.Dy_SpeakMButtonI = Gtk.Image()
        self.Dy_SpeakMButtonI.set_from_file(self.Dy_IconDir +
                                            "SpeakM_Icon_35.png")
        self.Dy_SpeakMButton.set_image(self.Dy_SpeakMButtonI)
        self.Dy_SpeakMButton.set_tooltip_text("Speak Little")
        self.Dy_SpeakMButton.set_size_request(35, 35)
        self.Dy_SpeakMButton.connect("clicked", self.Dy_SpeakLoud, 'S')

        self.Dy_Sperator = Gtk.Label()
        self.Dy_Sperator.set_name("Dy_Sperator")
        self.Dy_Sperator.set_size_request(854, 10)

        self.Dy_Spinner = Gtk.Spinner()
        self.Dy_Spinner.set_name("Dy_Spinner")

        self.Dy_StatusBottomOne = Gtk.Label()
        self.Dy_StatusBottomOne.set_label(self.Dy_StatusBottomOneText[0])
        self.Dy_StatusBottomOne.set_name("Dy_StatusBottom")

        self.Dy_StatusBottomTwo = Gtk.Label()
        self.Dy_StatusBottomTwo.set_label(self.Dy_StatusBottomTwoText[0])
        self.Dy_StatusBottomTwo.set_name("Dy_StatusBottom")

        self.Dy_StatusBottomThree = Gtk.Label()
        self.Dy_StatusBottomThree.set_label(self.Dy_StatusBottomThreeText[0])
        self.Dy_StatusBottomThree.set_name("Dy_StatusBottom")

        self.Dy_SpinnerSpeak = Gtk.Spinner()
        self.Dy_SpinnerSpeak.set_name("Dy_Spinner")
        self.Dy_SpinnerSpeak.start()

        self.Dy_HButtonBoxOne.pack_start(self.Dy_DummyStart, True, True, 0)
        self.Dy_HButtonBoxOne.pack_start(self.Dy_ListenButton, True, True, 0)
        self.Dy_HButtonBoxOne.pack_start(self.Dy_SearchButton, True, True, 0)
        self.Dy_HButtonBoxOne.pack_start(self.Dy_MoreButton, True, True, 0)
        self.Dy_HButtonBoxOne.pack_start(self.Dy_SpeakLButton, True, True, 0)
        self.Dy_HButtonBoxOne.pack_start(self.Dy_SpeakMButton, True, True, 0)
        self.Dy_HButtonBoxOne.pack_start(self.Dy_DummyEnd, True, True, 0)

        self.Dy_VBoxOne.pack_start(self.Dy_ResponseSmall, False, True, 0)
        self.Dy_VBoxOne.pack_start(self.Dy_MainImage, True, True, 0)

        self.Dy_HBoxTwo.pack_start(self.Dy_ResponseLarge, True, True, 0)
        self.Dy_HBoxTwo.pack_start(self.Dy_VBoxOne, True, True, 0)

        self.Dy_HBoxOne.pack_start(self.Dy_Spinner, True, True, 0)
        self.Dy_HBoxOne.pack_start(self.Dy_StatusBottomOne, True, True, 0)
        self.Dy_HBoxOne.pack_start(self.Dy_StatusBottomTwo, True, True, 0)
        self.Dy_HBoxOne.pack_start(self.Dy_StatusBottomThree, True, True, 0)
        self.Dy_HBoxOne.pack_start(self.Dy_SpinnerSpeak, True, True, 0)
        self.Dy_HBoxOne.set_size_request(854, 20)

        self.Dy_HBoxThree.pack_start(self.Dy_SwitchOffButton, False, False, 0)
        self.Dy_HBoxThree.pack_start(self.Dy_UserQuery, True, True, 0)
        self.Dy_HBoxThree.pack_start(self.Dy_TopLabelDummy, True, True, 0)

        self.Dy_VBoxTwo.pack_start(self.Dy_HBoxThree, True, True, 0)
        self.Dy_VBoxTwo.pack_start(self.Dy_HBoxTwo, True, True, 0)
        self.Dy_VBoxTwo.pack_start(self.Dy_UserEntry, True, True, 0)
        self.Dy_VBoxTwo.pack_start(self.Dy_HButtonBoxOne, True, True, 0)
        self.Dy_VBoxTwo.pack_start(self.Dy_Sperator, True, True, 0)
        self.Dy_VBoxTwo.pack_start(self.Dy_HBoxOne, True, True, 0)

        self.Dy_ScrollWindow.add_with_viewport(self.Dy_VBoxTwo)
        self.set_focus(self.Dy_UserEntry)
