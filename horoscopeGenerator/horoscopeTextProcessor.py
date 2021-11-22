# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 18:54:31 2021

@author: pmjum
"""
#A file for removing the limiters I put in 


filename = "horoscopeTextRaw.txt"
outFilename = "horoscopeTextProcessed.txt"


with open(filename,"r") as inFile:
    with open(outFilename,"w") as outFile:
        for line in inFile:
            if(not "-----" in line):
                line = line.rstrip("\n")
                line = line.strip()
                outFile.write(line)
    
print("done writing")