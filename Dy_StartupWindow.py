#!/usr/bin/env python3
import os
from gi.repository import Gtk, Gdk

class Dy_StarupWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dyctionary Startup")
        self.Dy_IconDir = os.getcwd() + "/Icons/"
        self.set_icon_from_file(self.Dy_IconDir + "DyLogo.png")

        self.Dy_SplashImage = Gtk.Image()
        self.Dy_SplashImage.set_from_file(self.Dy_IconDir + "StartUp.jpg")
        self.Dy_SplashImage.set_size_request(640, 400)

        self.add(self.Dy_SplashImage)
        self.set_decorated(False)
        self.set_position(Gtk.WindowPosition.CENTER)

def main():
    dyStartupWindow = Dy_StarupWindow()
    dyStartupWindow.connect("delete-event", Gtk.main_quit)
    dyStartupWindow.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
    
