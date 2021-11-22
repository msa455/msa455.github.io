# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 23:00:16 2021

@author: pmjum
"""

from bs4 import BeautifulSoup
import urllib.request
import datetime


#iterate through the posts on horoscope.com
#site structure:
    #by date:
        #by sign

#this is the URL style for horoscope.com        
test = "https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=1&laDate=20210701"

def parseSoup(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"lxml")
    text = soup.find("div",{"class":"main-horoscope"}).p.getText()
    return text.split("-")[1]

def urlBuilder(sign,date):
    dateString = "".join(date.strftime("%Y/%m/%d").split("/"))
    newUrl = "https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign=" + str(sign) + "&laDate=" + dateString
    return newUrl    
        
def scrapeHoroscopes():
    currentDate = datetime.date.today()
    #min Billboard Date: 1958,8,4
    minDate = currentDate - datetime.timedelta(days=365)
    with open("horoscopeTextRaw.txt","w") as file:
        while(currentDate >= minDate):
            print("fetching data for: ", str(currentDate), "...")
            for x in range(12):
                newUrl = urlBuilder(x+1,currentDate)
                text = parseSoup(newUrl)
                file.write(text)
            currentDate -= datetime.timedelta(days=1)    
    print("Data fetching complete!")


# =============================================================================
# today = datetime.datetime.now()
# minDate = today - datetime.timedelta(days=365)
# while(today >= minDate):
#     print(today)
#     today-=datetime.timedelta(days=1)
# =============================================================================
#print("".join(today.strftime("%Y/%m/%d").split("/")))
#yearAgo = today - datetime.timedelta(days=365)
#print(today)
#print(yearAgo)


scrapeHoroscopes()
#parseSoup(test)


