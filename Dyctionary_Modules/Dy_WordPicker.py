#!usr/bin/python3
import time
"""
Instance based
Class-name:        DyWordPicker-- Dyctionary Word Picker
module-name:       WordPicker.py
callable function: DyWrdPkr--->arguments(List, String)
"""

__author__ = "Jana_SR"

class DyWordPicker:
    def __init__(self):
        self.DyWrdPkrSmashList = []                     #Dyctionary Word Picker Smash List[list]
        self.DyWrdPkrSmasher = 0                        #Dyctionary Word Picker Smasher[number]
        self.DyWrdPkrList = []                          #Dyctionary Word Picker List[list]
        self.DyWrdPkrW = ''                             #Dyctionary Word Picker Received Word from other module[string word][before processing]
        self.DyWrdPkrWList = []                         #Dyctionary Word Picker Received Word List from other module[list][before processing]
        self.DyWrdPkrPointList = []
        self.DyWrdPkrPointListMain = []
        self.DyWrdPkrResult = ''
        self.DyWrdPkrStarPoints = 0
        self.DyWrdPkrSwapTemp = []
        self.DyWrdPkrTopper = 0
        self.DyWrdPkrTopperInList = []
        self.DyWrdPkrTopperRelation = 0
        self.DyWrdPkrToppersList = []
        self.DyWrdPkrTopperRelationList = []
        self.DyWrdPkrSmarter = ''

    def DyWrdPkrSwapperFunc(self, DySwapList):
        self.DyWrdPkrSwapList = []
        self.DyWrdPkrSwapTemp = []
        self.DyWrdPkrSwapList = DySwapList

        for DWPSLOut in range(len(self.DyWrdPkrSwapList)):
            for DWPLIn in range(len(self.DyWrdPkrSwapList)):
                if DWPLIn < (len(self.DyWrdPkrSwapList)-1):
                    if self.DyWrdPkrSwapList[DWPLIn][0] < self.DyWrdPkrSwapList[DWPLIn + 1][0]:
                        self.DyWrdPkrSwapTemp = self.DyWrdPkrSwapList[DWPLIn]
                        self.DyWrdPkrSwapList[DWPLIn] = self.DyWrdPkrSwapList[DWPLIn + 1]
                        self.DyWrdPkrSwapList[DWPLIn + 1] = self.DyWrdPkrSwapTemp

        return self.DyWrdPkrSwapList
        

    def DyWrdPkr(self, DyWrdPkrList, DyWrdPkrW):
        self.DyWrdPkrSmashList = []
        self.DyWrdPkrSmasher = 0
        self.DyWrdPkrList = []
        self.DyWrdPkrW = ''
        self.DyWrdPkrWList = []
        self.DyWrdPkrPointList = []
        self.DyWrdPkrPointListMain = []
        self.DyWrdPkrResult = ''
        self.DyWrdPkrStarPoints = 0
        self.DyWrdPkrSwapTemp = []
        self.DyWrdPkrTopper = 0
        self.DyWrdPkrTopperInList = []
        self.DyWrdPkrTopperRelation = 0
        self.DyWrdPkrToppersList = []
        self.DyWrdPkrTopperRelationList = []
        self.DyWrdPkrSmarter = ''
        self.DyWrdPkrSmashList = DyWrdPkrList
        self.DyWrdPkrW = DyWrdPkrW
        
        

        for DyWPS in range(len(self.DyWrdPkrSmashList)):
            self.DyWrdPkrSmasher = abs((abs((len(self.DyWrdPkrSmashList[DyWPS]) - len(self.DyWrdPkrW))) / 100) * 100 - 100)
            self.Dy_ThrowError = True
            if self.DyWrdPkrSmasher > 95:
                self.DyWrdPkrList.append(self.DyWrdPkrSmashList[DyWPS])
                self.Dy_ThrowError = False
        if self.Dy_ThrowError:
            return "No Matches found"
        
        
        for DyWPLp1 in range(0, len(self.DyWrdPkrList)):
            self.DyWrdPkrPointList = []
            self.DyWrdPkrStarPoints = 0
            self.DyWrdPkrWList = []

            for WLp in self.DyWrdPkrList[DyWPLp1]:
                self.DyWrdPkrWList.append(WLp)


            if len(self.DyWrdPkrList[DyWPLp1]) >= len(self.DyWrdPkrW):
                for DyWPLp1In in range(len(self.DyWrdPkrW)):

                    if self.DyWrdPkrList[DyWPLp1][DyWPLp1In] == self.DyWrdPkrW[DyWPLp1In]:

                        if DyWPLp1In == 0:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 10.9
                        elif DyWPLp1In == 1:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 8.8
                        elif DyWPLp1In == 2:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 5.5
                        elif DyWPLp1In == 3:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 2.2
                        elif DyWPLp1In == 4:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 2.2
                        else:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 2.0

                for DyWPLp1In2 in range(len(self.DyWrdPkrW)):
                    if self.DyWrdPkrW[DyWPLp1In2] in self.DyWrdPkrWList:
                        self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 0.25
                        self.DyWrdPkrWList.remove(self.DyWrdPkrW[DyWPLp1In2])
                        
                self.DyWrdPkrPointList.append(self.DyWrdPkrStarPoints)
                self.DyWrdPkrPointList.append(self.DyWrdPkrList[DyWPLp1])

            if len(self.DyWrdPkrList[DyWPLp1]) < len(self.DyWrdPkrW):
                for DyWPLp1In in range(len(self.DyWrdPkrList[DyWPLp1])):

                    if self.DyWrdPkrList[DyWPLp1][DyWPLp1In] == self.DyWrdPkrW[DyWPLp1In]:

                        if DyWPLp1In == 0:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 10.9
                        elif DyWPLp1In == 1:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 8.8
                        elif DyWPLp1In == 2:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 5.5
                        elif DyWPLp1In == 3:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 2.2
                        elif DyWPLp1In == 4:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 2.2
                        else:
                            self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 2.0

                for DyWPLp1In2 in range(len(self.DyWrdPkrW)):
                    if self.DyWrdPkrW[DyWPLp1In2] in self.DyWrdPkrWList:
                        self.DyWrdPkrStarPoints = self.DyWrdPkrStarPoints + 0.25
                        self.DyWrdPkrWList.remove(self.DyWrdPkrW[DyWPLp1In2])

                self.DyWrdPkrPointList.append(self.DyWrdPkrStarPoints)
                self.DyWrdPkrPointList.append(self.DyWrdPkrList[DyWPLp1])

            self.DyWrdPkrPointListMain.append(self.DyWrdPkrPointList)
            

        self.DyWrdPkrPointListMain = self.DyWrdPkrSwapperFunc(self.DyWrdPkrPointListMain)

        self.DyWrdPkrTopper = self.DyWrdPkrPointListMain[0][0]

        if self.DyWrdPkrTopper == 0:
            self.DyWrdPkrSmarter = "No Result Found"
        else:
            for DWPTLp in range(len(self.DyWrdPkrPointListMain)):
                if self.DyWrdPkrTopper == self.DyWrdPkrPointListMain[DWPTLp][0]:
                    self.DyWrdPkrTopperRelation = abs((abs(len(self.DyWrdPkrPointListMain[DWPTLp][1]) - len(DyWrdPkrW)) / 100) * 100 - 100)
                    self.DyWrdPkrToppersList.append(self.DyWrdPkrTopperRelation)
                    self.DyWrdPkrToppersList.append(self.DyWrdPkrPointListMain[DWPTLp][1])
                    self.DyWrdPkrTopperRelationList.append(self.DyWrdPkrToppersList)

            self.DyWrdPkrTopperRelationList = self.DyWrdPkrSwapperFunc(self.DyWrdPkrTopperRelationList)
            self.DyWrdPkrSmarter = self.DyWrdPkrTopperRelationList[len(self.DyWrdPkrTopperRelationList) - 1][1]
        
        print(time.clock())                 
        return self.DyWrdPkrSmarter
        
def main():
    dw = DyWordPicker()
    myList = ['hello', 'hell', 'hear']
    myWord = 'helo'
    dw.DyWrdPkr(myList, myWord)
    
if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    