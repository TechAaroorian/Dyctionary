#!/usr/bin/env python3
myList = open("Dy_PhonemeList.txt", 'r')

myData = myList.read().split("\n")

myList.close()

myDataOne = [dat.lower().split(" ")[0] for dat in myData]
myDataTwo = ["-".join(dat.lower().split(" ")[1:]) for dat in myData]

newT = open("new.py", 'w')

newT.write("Dy_PhonemeList = {\n")
for i in range(len(myDataOne)):
    newT.write('    "' + myDataOne[i] + '" : "' + myDataTwo[i] + '",\n')
    
newT.write("}")

newT.close()
    
