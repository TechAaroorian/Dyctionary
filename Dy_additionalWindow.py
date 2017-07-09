#!/usr/bin/env python3
import sys
import os
from gi.repository import Gtk, Gdk
from Dyctionary_Modules.Dy_WordNetAccess import wordnetAccess

mainCss = b"""
        #mainWindow{
            background-color: black;
        }
        #allTitle{
            background-color:black;
            color: yellow;
            font-size: 18px;
            font-weight: bold;
            font-style: italic;
        }
        #two{
            background-color: #030b5a;
            color: white;
            border-radius: 14px;
            font-size: 16px;
        }
        #one{
            color: yellow;
            font-size: 14px;
        }
"""

class Dy_additionalWindow(Gtk.Window):
    def __init__(self, *mainWord):
        
        labelOne = mainWord[0]
        labelTwo = mainWord[1]
        labelFour = mainWord[2]
        labelSix = mainWord[3]
        mainTitle = mainWord[0] + " - Dyctionary Additional Window"
        
        self.Dy_IconDir = os.getcwd() + "/Icons/"
        self.Dy_SpeechRegPath = os.getcwd() + "/SpeechRecognition-Julius/"
        
        Gtk.Window.__init__(self, title=mainTitle)
        self.set_icon_from_file(self.Dy_IconDir + "DyLogo.png")
        self.set_default_size(1000, 600)
        self.set_size_request(400, 400)
        self.set_border_width(10)
        self.set_name("mainWindow")
        
        self.Dy_awLabelOne = Gtk.Label(labelOne)
        self.Dy_awLabelOne.set_name("allTitle")
        
        self.Dy_awLabelTwo = Gtk.Label()
        self.Dy_awLabelTwo.set_line_wrap(True)
        self.Dy_awLabelTwo.set_markup(labelTwo)
        self.Dy_awLabelTwo.set_size_request(800, 200)
        self.Dy_awLabelTwo.set_name("two")
        
        self.Dy_awLabelThree = Gtk.Label("Example Sentences")
        self.Dy_awLabelThree.set_name("one")
        
        self.Dy_awLabelFour = Gtk.Label()
        self.Dy_awLabelFour.set_line_wrap(True)
        self.Dy_awLabelFour.set_markup(labelFour)
        self.Dy_awLabelFour.set_size_request(800, 200)
        self.Dy_awLabelFour.set_name("two")
        
        self.Dy_awLabelFive = Gtk.Label("More related Words")
        self.Dy_awLabelFive.set_name("one")
        
        self.Dy_awLabelSix = Gtk.Label()
        self.Dy_awLabelSix.set_line_wrap(True)
        self.Dy_awLabelSix.set_label(labelSix)
        self.Dy_awLabelSix.set_size_request(800, 200)
        self.Dy_awLabelSix.set_name("two")
        
        #self.Dy_awStatus = Gtk.Statusbar(mainWord)
        
        self.Dy_awVBoxin = Gtk.VBox(spacing=6)
        #self.Dy_awVBoxin.pack_start(self.Dy_awLabelOne, True, True, 0)
        self.Dy_awVBoxin.pack_start(self.Dy_awLabelTwo, True, True, 0)
        self.Dy_awVBoxin.pack_start(self.Dy_awLabelThree, True, True, 0)
        self.Dy_awVBoxin.pack_start(self.Dy_awLabelFour, True, True, 0)
        self.Dy_awVBoxin.pack_start(self.Dy_awLabelFive, True, True, 0)
        self.Dy_awVBoxin.pack_start(self.Dy_awLabelSix, True, True, 0)
        
        self.Dy_awScrollWindow = Gtk.ScrolledWindow()
        self.Dy_awScrollWindow.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.Dy_awScrollWindow.add_with_viewport(self.Dy_awVBoxin)
        
        self.Dy_awVBox = Gtk.VBox(spacing=6)
        self.Dy_awVBox.pack_start(self.Dy_awLabelOne, False, False, 0)
        self.Dy_awVBox.pack_start(self.Dy_awScrollWindow, True, True, 0)
        #self.Dy_awVBox.pack_start(self.Dy_awStatus, True, True, 0)
        self.add(self.Dy_awVBox)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        self.Dy_StyleProvider = Gtk.CssProvider()
        self.Dy_StyleProvider.load_from_data(mainCss)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.Dy_StyleProvider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        
        

def main():
    DyAW = Dy_additionalWindow(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    DyAW.connect("delete-event", Gtk.main_quit)
    DyAW.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
