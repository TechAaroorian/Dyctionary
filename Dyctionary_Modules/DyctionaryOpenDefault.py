#!/usr/bin/env python3
import time
import random

class DyctionaryOpenDefault:
    def __init__(self, ):
        self.Dy_currentTime = int(str(time.ctime().split()[3]).split(":")[0])
        self.printTime()
    
    def printTime(self):
        print(self.Dy_currentTime)
        
def main():
    Dy_OD = DyctionaryOpenDefault()
    
if __name__ == '__main__':
    main()
    

