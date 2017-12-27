#!/usr/bin/env python
import random
import time
import subprocess
from Dyctionary_Modules.Dy_MagnetizerEssentials import DyMagnetizerEssentials
from Dyctionary_Modules.DyctionaryRamdomGenerator import DyRandomGenerator
from Dyctionary_Modules.Dy_WordNetAccess import wordnetAccess
from Dyctionary_Modules.Dy_CurrentDayEssentials import currentDayEssentials


class DyMagnetizer:
    def __init__(self):
        self.DyWAObject = wordnetAccess()
        self.Dyobject = DyMagnetizerEssentials()
        self.DycdeObject = currentDayEssentials()
        self.DyMagnetList = self.Dyobject.ListOne
        self.DyChat = self.Dyobject.chatResponse
        self.firstCheck = self.Dyobject.chatKey
        self.DyRandomObj = DyRandomGenerator()
        self.iterCheck = 0
        self.wordPosition = None

    def DyMangnetizerEvaluate(self, getString):
        self.sendResult = []
        self.iterCheck = 0
        self.queryString = getString
        self.splitValue = self.queryString.split(' ')

        if len(self.splitValue) == 1:
            self.sendResult = self.DyWAObject.nltkAccess(self.queryString)
            return self.sendResult

        if self.queryString in self.firstCheck:
            if self.DyChat[self.queryString] == 'call time module':
                self.resultList = self.getresultTime()
                return [self.resultList], None
            elif self.DyChat[self.queryString] == 'call date module':
                self.resultList = self.getresultDate()
            elif self.queryString == 'call day module':
                self.resultList = self.getresultDay()
            elif self.queryString == 'call joke module':
                self.resultList = self.getresultJoke()
            elif self.DyChat[self.queryString] == 'call mmn module':
                self.resultList = self.getresultMMN()
                subprocess.Popen(['espeak', '-v', 'f5', self.resultList], shell=False)
                return [self.resultList], False
            else:
                print("here")
                level = random.randint(0, len(self.DyChat[self.queryString]) - 1)
                self.resultList = self.DyChat[self.queryString][level]
                subprocess.Popen(['espeak',  '-s', '145', '-v', 'f5', self.resultList])
                return [self.resultList], None

        else:
            try:
                raiseException = True
                for currentList in self.DyMagnetList:
                    if len(self.splitValue) == len(currentList):
                        for currentPosition in range(len(currentList)):
                            if self.splitValue[currentPosition] == currentList[currentPosition]:
                                self.iterCheck = self.iterCheck + 1
                            else:
                                self.wordPosition = currentPosition

                    if self.iterCheck == (len(self.splitValue) - 1):
                        raiseException = False
                        self.sendResult, checkExist = self.DyWAObject.nltkAccess(self.splitValue[self.wordPosition])
                        return self.sendResult, checkExist

                if raiseException:
                    raise Exception

            except Exception as e:
                subprocess.Popen(['espeak', '-v', 'f5', '-s', '145', "Sorry.. I cannot understand"])
                print(e)
                return ['Sorry.. I cannot understand'], False

    def getresultTime(self):
        subprocess.Popen(['killall', 'espeak'], shell=False)
        subprocess.Popen(['espeak', '-v', 'f5', self.DycdeObject.getTimeEssentials()[1]], shell=False)
        return self.DycdeObject.getTimeEssentials()[0]

    def getresultMMN(self):
        currentTime = self.DycdeObject.getTimeEssentials()[4]
        checkStatus = ''
        attach = ''
        position = random.randint(0, 3)
        returnReslt = ''

        if currentTime < 12:
            checkStatus = 'good morning'
            returnReslt = self.Dyobject.goodMorning[position]
            attach = 'morning'
        elif currentTime > 12 and currentTime < 16:
            checkStatus = 'good afternoon'
            returnReslt = self.Dyobject.goodAfternoon[position]
            attach = 'afternoon'
        elif currentTime > 16 and currentTime < 20:
            checkStatus = 'good evening'
            returnReslt = self.Dyobject.goodEvening[position]
            attach = 'evening'
        elif currentTime > 20:
            checkStatus = 'good night'
            returnReslt = self.Dyobject.goodNight[position]
            attach = 'night'

        if self.queryString == checkStatus:
            return returnReslt
        else:
            position = random.randint(0, 3)
            randomResponse = ('This seems ' + attach,
                              "It is not " + self.queryString.split(" ")[1] + ". It is " + attach,
                              "Are you kidding me.. It is not " + self.queryString.split(" ")[1],
                              "Are you joking.. It is " + attach)

            return randomResponse[position]
