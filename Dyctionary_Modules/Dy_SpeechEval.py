
class DySpeechEval:
    
    def __init__(self, ):
        self.Dy_MainReturnOutput = []
        self.Dy_MainInputList = []
        self.Dy_MainInputLen = 0
        self.Dy_MainInputFLLen = 0
    
    def Dy_SpeechEvalAnalyzeInput(self, Dy_MainInput):
        self.Dy_MainInput = Dy_MainInput.strip().lower()
        self.Dy_MainInputList = self.Dy_MainInput.split(" ")
        self.Dy_MainInputLen = len(self.Dy_MainInputList)
        
        if self.Dy_MainInputLen != 1:
            self.Dy_MainInputFLLenOne = len(self.Dy_MainInputList[0])
            self.Dy_MainInputFLLenTwo = len(self.Dy_MainInputList[1])
            
        if self.Dy_MainInputLen == 1:
            pass
        elif self.Dy_MainInputFLLenOne == 1 and self.Dy_MainInputFLLenTwo == 1:
            pass
        
        
        
        
    
        
    
