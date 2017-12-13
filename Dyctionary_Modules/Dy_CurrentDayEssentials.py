#!/usr/bin/env python3
import time
import subprocess


class currentDayEssentials:
    def __init__(self):
        """self.todayDay = self.allDays[self.allTimeResult[0]]
        self.todayMonth = self.allTimeResult[1]
        self.todayYear = self.allTimeResult[4]
        self.startingTime = self.allTimeResult[3].split(":")[0]"""

        self.allDays = {
            'Sun': 'sunday',
            'Mon': 'monday',
            'Tue': 'tuesday',
            'Wed': 'wednesday',
            'Thu': 'thursday',
            'Fri': 'friday',
            'Sat': 'saturday'
        }

        self.allMonths = {
            'Jan': ['January', '31', '1'],
            'Feb': ['February', '28 or 29', '2'],
            'Mar': ['March', '31', '3'],
            'Apr': ['April', '30', '4'],
            'May': ['May', '31', '5'],
            'Jun': ['June', '30', '6'],
            'Jul': ['July', '31', '7'],
            'Aug': ['August', '31', '8'],
            'Sep': ['September', '30', '9'],
            'Oct': ['October', '31', '10'],
            'Nov': ['November', '30', '11'],
            'Dec': ['December', '31', '12']
        }

        self.IntroBig = None
        """
        if self.startingTime < 12:
            self.IntroBig = 'good Morning'
        elif self.startingTime > 12 and self.startingTime < 16:
            self.IntroBig = 'good afternoon'
        elif self.startingTime > 16 and self.startingTime < 19:
            self.IntroBig = 'good evening'
        else:
            self.IntroBig = 'gradual'
         """
        #self.getTimeEssentials()

    def getTimeEssentials(self):
        splittedTimeString = time.ctime().split(" ")
        normalizedTimeString = []

        for currentValue in splittedTimeString:
            if currentValue != '' and currentValue != " ":
                normalizedTimeString.append(currentValue)

        todayDay = self.allDays[normalizedTimeString[0]]
        todayMonth = self.allMonths[normalizedTimeString[1]][0]
        todayDate = normalizedTimeString[2]
        todayTime = int(normalizedTimeString[3].split(":")[0])
        sendRailyWayTime = todayTime
        todayYear = normalizedTimeString[4]

        currentTimeCal = normalizedTimeString[3].split(":")

        if todayTime > 12:
            todayTime = todayTime - 12
            currentMode = ("PM", "P, M")
        else:
            currentMode = ("AM", "A, M")

        currentTime = str(
            todayTime) + ":" + currentTimeCal[1] + " " + currentMode[0]
        currentTimeSpeech = "Time is, " + str(
            todayTime) + " " + currentTimeCal[1] + " " + currentMode[1]

        todayFullDate = todayMonth + " " + todayDate + " " + todayYear
        todayFullDateSpeech = todayMonth + ", " + todayDate + ", " + todayYear

        return [
            currentTime, currentTimeSpeech, todayFullDate, todayFullDateSpeech,
            sendRailyWayTime
        ]
