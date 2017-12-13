#!/usr/bin/env python3


class DyWordPredictor:
    def __init__(self, ):
        self.DyPoints = (9.9, 7.7, 6.6, 5.5, 4.4, 2.5)

    def DyWordPredictorMain(self, DyWordPredList, DyWordPredWord):
        self.DyWordPredList = DyWordPredList
        self.DyWordPredWord = DyWordPredWord
        self.DyWordPredPoints = {}
        self.DyWordPredKey = []

        self.DyWordPredSmasher = 0
        self.DyWordPredSmashList = []
        self.DyWordPredListOne = []
        self.DyWordPredStopFurther = True

        for loopOneCurrentElement in self.DyWordPredList:
            self.DyWordPredSmasher = abs(
                (len(loopOneCurrentElement) - len(self.DyWordPredWord) / 100) *
                100 - 100)
            if self.DyWordPredSmasher > 95:
                self.DyWordPredListOne.append(loopOneCurrentElement)
                self.DyWordPredStopFurther = False

        if self.DyWordPredStopFurther:
            raise Exception

        for loopTwoCurrenElement in self.DyWordPredListOne:
            self.DyWordPredPointsNum = 0

            if len(loopTwoCurrenElement) < len(self.DyWordPredWord):
                self.loopLength = len(loopTwoCurrenElement)
            else:
                self.loopLength = len(self.DyWordPredWord)

            for loopCurrentPosition in range(self.loopLength):
                if loopTwoCurrenElement[
                        loopCurrentPosition] == self.DyWordPredWord[
                            loopCurrentPosition]:
                    if loopCurrentPosition < 5:
                        self.DyWordPredPointsNum = self.DyWordPredPointsNum + self.DyPoints[loopCurrentPosition]
                    else:
                        self.DyWordPredPointsNum = self.DyWordPredPointsNum + self.DyPoints[5]

            for loopCurrentLetter in self.DyWordPredWord:
                if loopCurrentLetter in loopTwoCurrenElement:
                    self.DyWordPredPointsNum = self.DyWordPredPointsNum + 0.25

            self.DyWordPredPoints[
                self.DyWordPredPointsNum] = loopTwoCurrenElement

        self.DyWordPredKey = sorted(list(self.DyWordPredPoints.keys()))[-1]

        return self.DyWordPredPoints[self.DyWordPredKey]
