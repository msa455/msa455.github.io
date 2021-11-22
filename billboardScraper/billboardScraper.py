# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:52:57 2021

@author: pmjum
"""

from bs4 import BeautifulSoup
import requests
import os
import datetime
import time
import pandas as pd
from lyricsgenius import Genius
import readability



token = "INSERT_GENIUS_API_KEY_HERE"
genius = Genius(token)


weeks = ["2021-05-29", "2021-05-22", "2021-05-15"]

#TODO: Add logic checking if the file exists and what state it is at
outputFile = "billboardData.csv"
 
#A helper function that pings google to check if our connection is offline. 
def checkConnection():
    #ping google, if response, return True
    return True

#get names of the artists and songs from between the brackets
def getNames(text):
    text = text.replace(">","<")
    text = text.split("<")
    return(text[2])

#add all of the info for that week to an array and return the array
def addWeek(week, names, artists,rankNumbers):
    allData = []
    for i in range(len(names)):
        name = getNames(str(names[i]))
        if "," in name:
            name = name.replace(",", "|")
        rankNumber = getNames(str(rankNumbers[i]))
        artist = getNames(str(artists[i]))
        if "," in artist:
            artist = artist.replace(","," &amp; ")
        entry = week + "," + name + "," + artist + "," + rankNumber
        allData.append(entry)
        
    return allData

#get the songnames, artists, and rank number for a given week
def getSoup(week):
    url = "https://www.billboard.com/charts/hot-100/" + week
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    songNames = soup.find_all("span", {"class":"chart-element__information__song"})
    artists = soup.find_all("span", {"class":"chart-element__information__artist"})
    rankNumber = soup.find_all("span", {"class":"chart-element__rank__number"})
    return(songNames,artists,rankNumber)


                
def makeCSV(outputFile):
    with open(outputFile, "w") as f:
        currentDate = datetime.date.today()
        #min Billboard Date: 1958,8,4
        minDate = datetime.date(1958,8,4)
        oneWeek = datetime.timedelta(days=7)
        while(currentDate >= minDate):
            print("fetching data for: ", str(currentDate), "...")
            songNames,artists,rankNumbers = getSoup(str(currentDate))
            data = addWeek(str(currentDate),songNames,artists,rankNumbers)
            for song in data:
                f.write(song + "\n")
            currentDate -= oneWeek
            time.sleep(2)


def stripLyrics(lyrics):
    lyrics = lyrics.split("\n")
    lastLine = lyrics[-1].split(" ")
    if("URLCopyEmbedCopy") in lastLine:
        lastLine = lastLine[:-2]
        lyrics[-1] = " ".join(lastLine)

    cleanedLyrics = []
    for line in lyrics:
        if("[" not in line):
            cleanedLyrics.append(line)
    return "\n".join(cleanedLyrics)

def getLyrics(title,artist):
    song = genius.search_song(title,artist)
    if hasattr(song, "lyrics"):
        return stripLyrics(song.lyrics)
    else:
        print("no lyrics found")
        song = genius.search_song(title)
        try:
            return stripLyrics(song.lyrics)
        except AttributeError:
            return False

def getReadingLevels(text):
    result = readability.getmeasures(text, lang="en")
    levels = []
    for item in result["readability grades"]:
        levels.append(result["readability grades"][item])
    return levels


#print(getReadingLevels(getLyrics("Good 4 U","Olivia Rodrigo")))

def compileReadingLevels(infile, bulkfile, outfile):
    with open(infile, "r") as readFile:
        with open(bulkfile,"w",encoding="utf-8") as bulkFile:
            with open(outfile, "w") as writeFile:
                #these are the levels for the different tests, they are in the following order:
                #Flesch Kincaid Grade Level, ARI, Coleman-Liau, FleschReadingEase, GunningFOG
                #LIX, SMOGindex, RIX, DaleChallIndex
                writeFile.write("Week,Title,Artist,Rank,Flesh-Kincaid,ARI,Coleman-Liau,FleschReadingEase,GunningFOG,LIX,SMOGindex,RIX,DaleChallIndex \n")
    
                numEntries = 0            
                for index,line in enumerate(readFile):
                    if(numEntries%100==0):
                        print("Finished collecting lyrics for ", numEntries, " songs so far")
                    line = line.split(",")
                    try :
                        lyrics = getLyrics(line[1],line[2])
                    except: 
                        pass
                    if(lyrics):
                        levels = getReadingLevels(lyrics)
                        
                        line = ",".join(map(lambda x: x.strip("\n"),line)) + "," + ",".join(map(str,levels)) + "\n"
                        #print(line)
                        writeFile.write(line)
                        bulkFile.write(line)
                        bulkFile.write(lyrics)
                        bulkFile.write("---------")
                        numEntries += 1
                    else:
                        pass
        print("Completed searching for lyrics. Found lyrics information for ", numEntries, "songs")
                
    

compileReadingLevels("billboardData.csv","lyrics.txt", "billboardDataWithReadingLevels.csv")

#print(getReadingLevels(getLyrics("Good 4 U","Olivia Rodrigo")))
#compileReadingLevels(outputFile,"readingLevels.csv")
#print(getLyrics("Leave The Door Open", "Silk Sonic (Bruno Mars & Anderson .Paak)"))

#print(getSongNames(str(songNames[0])))


#makeCSV(outputFile)

#df = pd.read_csv("test.csv")

#print(df.tail(1))