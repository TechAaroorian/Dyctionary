#!/usr/bin/env python3
import sqlite3

myConn = sqlite3.connect("Dy_AllWords.py")

myCur = myConn.cursor()

myWord = input("Enter the word: ")
