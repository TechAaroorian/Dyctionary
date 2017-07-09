#!/usr/bin/env python3
from Dyctionary_Modules.Dy_Magnetizer import DyMagnetizer
from Dyctionary_Modules.Dy_WordPredictor import DyWordPredictor
import enchant
import subprocess

class Dy_UserEntryAnalyzer:
    def __init__(self):
        self.Dy_EnchantDict = enchant.Dict('en-Us')
        self.Dy_WordPickerObject = DyWordPredictor()
        self.Dy_MagnetizerObject = DyMagnetizer()
        self.Dy_SentenceSplit = []
        self.Dy_FinalResult = []
        self.Dy_EnchantSuggestList = []
        self.Dy_ExpressionEvalList = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '', ' ', '+', '-', '*', '/', '%', '(', ')')
        self.Dy_TakeSecondDecision = False
        
    def Dy_ResponseInstant(self, Dy_UserEntrySentence):
        try:
            self.Dy_FinalResult = []
            self.Dy_SentenceSplit = Dy_UserEntrySentence.split(" ")
            self.Dy_UserEntrySentence = Dy_UserEntrySentence
            
            for DyEntry in self.Dy_SentenceSplit:
                if len(DyEntry) < 3:
                    self.Dy_FinalResult.append(DyEntry)
                elif self.Dy_EnchantDict.check(DyEntry):
                    self.Dy_FinalResult.append(DyEntry)
                else:
                    Dy_EnchantSuggestList = self.Dy_EnchantDict.suggest(DyEntry)
                    for elem in Dy_EnchantSuggestList:
                        if ' ' not in elem:
                            self.Dy_EnchantSuggestList.append(elem)
                    
                    Result = self.Dy_WordPickerObject.DyWordPredictorMain(self.Dy_EnchantSuggestList, DyEntry)
                    self.Dy_FinalResult.append(Result)
                    
            return (" ").join(self.Dy_FinalResult)
        except Exception as e:
            raiseError = False
            for checkData in self.Dy_UserEntrySentence:
                if checkData in self.Dy_ExpressionEvalList:
                    pass
                else:
                    raiseError = True
            if raiseError:
                return "Unexpected symbols or numbers"
            else:
                return self.Dy_UserEntrySentence
        
    def Dy_Evaluation(self, Dy_UserEntrySentence):
        try:
            self.Dy_UserEntrySentence = Dy_UserEntrySentence.split(" ")
            
            self.Normalized = []
            for currentValue in self.Dy_UserEntrySentence:
                if currentValue != "" and currentValue != " ":
                    self.Normalized.append(currentValue)
                
            self.Dy_EvaluationGen = [symbs for symbs in ''.join(self.Normalized)]
            
            for symbs in self.Dy_EvaluationGen:
                if symbs not in self.Dy_ExpressionEvalList:
                    self.Dy_TakeSecondDecision = True
                    break
                
            if self.Dy_TakeSecondDecision:
                checkExist = None
                self.Dy_EvalCorrected = self.Dy_ResponseInstant(" ".join(self.Normalized))
                self.sendResult, checkExist = self.Dy_MagnetizerObject.DyMangnetizerEvaluate(self.Dy_EvalCorrected)
                return self.sendResult, checkExist
            else:
                result = str(eval(''.join(self.Dy_EvaluationGen)))
                speakArithmetic = ''
                
                for allVal in result:
                    if allVal == '.':
                        speakArithmetic = speakArithmetic + "point" + " "
                    else:
                        speakArithmetic = speakArithmetic + allVal + " "
                
                speakArithmetic = "answer is, " + speakArithmetic
                sendListOne = "Answer is: " + result
                subprocess.Popen(['espeak', '-v', 'f5', speakArithmetic], shell=False)
                return [sendListOne], None
        except Exception as e:
            print("Here")
        
    