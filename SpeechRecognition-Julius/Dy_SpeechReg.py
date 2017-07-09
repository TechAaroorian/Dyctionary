#!/usr/bin/env python3


def main():
    Dy_CacheSentence = ""
    Dy_Raw = ""
    Dy_RawList = []
    
    while True:
        Dy_Raw = ""
        Dy_RawList = []
        Dy_Raw = input()
        
        if 'sentence1' in Dy_Raw:
            Dy_RawList = Dy_Raw.split(" ")
            
            Dy_CacheSentence = ""
            for i in range(len(Dy_RawList)):
                if i != 0 and i != 1 and i != (len(Dy_RawList) - 1):
                    Dy_CacheSentence = Dy_CacheSentence + Dy_RawList[i] + " "
                    
                    with open("Dy_SpeechReg.output", 'w') as Dy_Output:
                        Dy_Output.write(Dy_CacheSentence)
                                    
        
if __name__ == '__main__':
    main()