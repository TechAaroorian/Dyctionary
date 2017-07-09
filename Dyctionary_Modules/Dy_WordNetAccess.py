#!/usr/bin/env python3
import Dyctionary_Modules.AllPhoneme as AllPhoneme
from nltk.corpus import wordnet
import enchant
import random
import subprocess


class wordnetAccess:
    def __init__(self):
        self.myDict = enchant.Dict('en-US')
        self.numberOfSenses = 0
        self.mainWord = ''
        self.wordOfTheDay = ''
        self.finalWord = ''
        self.suggetList = []
        self.allLetters = ('a', 'b', 'c', 'd',
                           'e', 'f', 'h', 'i',
                           'j', 'k', 'l', 'm',
                           'n', 'o', 'q', 'r',
                           't', 'u', 'w', 'x',
                           'y', 'z')
        
        self.randomLetterlength = random.randrange(3, 8)
        
        for value in range(self.randomLetterlength):
            self.wordOfTheDay = self.allLetters[random.randrange(0, 21)] + self.wordOfTheDay
            
        self.suggestList = self.myDict.suggest(self.wordOfTheDay)
        self.finalWord = self.suggestList[random.randrange(len(self.suggestList))]
        
        
        
    def nltkAccess(self, myWord):
        self.mainWord = myWord
        #self.mainWord = "<span font='22' color='orange" + self.mainWord + "</span>"
        self.synsetsCurrentWord = wordnet.synsets(myWord)
        self.numberOfSenses = len(self.synsetsCurrentWord)
        self.allSences = [] 
        self.allDefinitions = ''
        self.allDefinitionSpeech = ''
        self.allExamples = []
        self.selectedExamples = []
        self.selectedExampleString = ''
        self.allLemmas = []
        self.everyDefinitions = []
        self.everyDefinitionSpeechs = []
        self.everyExamples = []
        self.allLemmaString = ''
        self.sentenceString = ''
        self.responseTalkMany = ('There are ' + str(self.numberOfSenses) + " meanings for word '" + self.mainWord + "'. ",
                                "I've found " + str(self.numberOfSenses) + " meanings for word '" + self.mainWord + "'. ",
                                str(self.numberOfSenses) + " meanings picked for word '" + self.mainWord + "'. ",
                                "'" + self.mainWord + "' has " + str(self.numberOfSenses) + " meanings. ",
        )
        
        self.responseTalkOne = ("There is only one meaning for word '" + self.mainWord + "'. ",
                                "I've got one meaning for word '" + self.mainWord + "'. ",
                                "Only one meaning for word '" + self.mainWord + "'. ",
                                "Not many, only one meaning found for '" + self.mainWord + "'. "
        )
        
        self.prettyTalkResponse = ("Seems, pretty much meanings available. ",
                                   "Really good count of meanings. ",
                                   'Great, '
        )
        
        self.excessTalkResponse = ("Wow..  ",
                                   "OMG..  ",
                                   "Really hunge count of meanings available. "
        )
        
        self.extendTalk = ("To access more details use 'more' option, because given this answers are more concise for some words. ",
                           "This is too concise definition and meanings here, to access related words and more. Use 'more' option. ",
                           "I can read the meanings of the words, if you like. Use speak buttons. ",
                           "I can understand your sentences as much as possible, so you can chat somethings. I won't ever annoy you. ",
                           "Difficult to do long arthmetic? Leave it to me, I can understand math expressions. ")
        position = random.randint(0, 3)
        if self.numberOfSenses > 1:
            self.sentenceString = self.responseTalkMany[position]
            
            if self.numberOfSenses > 7 and self.numberOfSenses < 20:
                position = random.randint(0, 2)
                self.sentenceString = self.prettyTalkResponse[position]+ self.sentenceString
            elif self.numberOfSenses > 20:
                position = random.randint(0, 2)
                self.sentenceString = self.excessTalkResponse[position] + self.sentenceString
        elif self.numberOfSenses == 1:
            self.sentenceString = self.responseTalkOne[position]
        else:
            self.sentenceString = "Sorry... No meaning found for <span font='20' color='orange'><i>" + self.mainWord + ". </i></span>Wordnet database does have source for it. "
            self.sentenceString = self.sentenceString + "It may not be a vocabulary or new terminology."
            
            sendListOne = "<b>" + self.sentenceString + "</b>"
            sendListTwo = "Ooops..."
            sendListFour = "No Source Found"
            
            return [sendListOne, sendListTwo, None, sendListFour], True
        
        for currentValue in self.synsetsCurrentWord:
            self.allSences.append(str(currentValue).split("'")[1])
            
        for currentIter in range(2):
            self.allDefinitions = ''
            self.allDefinitionSpeech = ''
            if currentIter == 0:
                putRange = len(self.allSences)
            else:
                if len(self.allSences) > 7:
                    putRange = 7
                else:
                    putRange = len(self.allSences)
                    
            for currentPosition in range(putRange):
                self.allDefinitions = self.allDefinitions + "\t<span color='#bccbf4'>Meaning " + str(currentPosition + 1) + ")</span>   "
                self.allDefinitions = self.allDefinitions + wordnet.synset(self.allSences[currentPosition]).definition()
                self.allDefinitions = self.allDefinitions + " <span color='orange'><b>(" + self.allSences[currentPosition].split(".")[1] + ")</b></span>\n"
                self.allDefinitionSpeech = self.allDefinitionSpeech + "Meaning" + str(currentPosition + 1) + ", - ,"
                self.allDefinitionSpeech = self.allDefinitionSpeech + wordnet.synset(self.allSences[currentPosition]).definition()
                if len(self.allSences) > currentPosition:
                    self.allDefinitionSpeech = self.allDefinitionSpeech + ", - , - , - ,"
                else:
                    self.allDefinitionSpeech = self.allDefinitionSpeech + ","
            
            self.everyDefinitions.append(self.allDefinitions)
            self.everyDefinitionSpeechs.append(self.allDefinitionSpeech)
            
        for currentValue in self.allSences:
            self.allExamples = self.allExamples + wordnet.synset(currentValue).examples()
            self.allLemmas = self.allLemmas + wordnet.synset(currentValue).lemma_names()
        
        self.allLemmas = set(self.allLemmas)
        
        if len(self.allLemmas) == 0:
            self.allLemmaString = "Sorry No related words found"
        else:
            for currentSetValue in self.allLemmas:
                if currentSetValue != myWord:
                    self.allLemmaString = self.allLemmaString + currentSetValue + ",    "
        
        if len(self.allExamples) == 0:
            self.sentenceString = self.sentenceString + " No Examples found. "
            self.selectedExampleString = ''
            self.allExampleString = " There is no examples found."
        else:
            for currentValue in self.allExamples:
                splitValue = currentValue.split(" ")
                if myWord in splitValue:
                    self.selectedExamples.append(currentValue)
                    
            if len(self.selectedExamples) == 0:
                if len(self.allExamples) > 2:
                    stopSlice = 2
                else:
                    stopSlice = len(self.allExamples)
                    
                self.selectedExamples = self.allExamples[0:stopSlice]
            else:
                if len(self.selectedExamples) > 2:
                    stopSlice = 2
                else:
                    stopSlice = len(self.selectedExamples)
                    
                self.selectedExamples = self.selectedExamples[0:stopSlice]
            self.selectedExampleString = "<span font='18' color='#3ec1ec'><b>Example Sentences:</b></span>\n\n\t" + "\n\t".join(self.selectedExamples)
            self.allExampleString = "\n".join(self.allExamples)
                
                         
        #subprocess.Popen(['espeak', '-s', '145', '-v', 'f5', self.everyDefinitionSpeechs[1]])
        hintPosition = random.randint(0, 4)
        sendListOne = "<span font='18' color='#3ec1ec'><b>" + self.sentenceString + self.extendTalk[hintPosition] + "</b></span>"
        sendListOne = sendListOne + "\n\n" + self.everyDefinitions[1] + "\n\n" + self.selectedExampleString
        sendListTwo = AllPhoneme.Dy_PhonemeList[self.mainWord]
        sendListThree = self.everyDefinitionSpeechs[1]
        sendListFour = self.mainWord
        sendListFive = self.allExampleString
        sendListSix = self.everyDefinitions[0]
        sendListSev = self.allLemmaString

        return [sendListOne, sendListTwo, sendListThree, sendListFour, sendListFive, sendListSix, sendListSev], False


    def randomWordInit(self):
        returnData, check = self.nltkAccess(self.finalWord)
        
        return returnData, check

        
