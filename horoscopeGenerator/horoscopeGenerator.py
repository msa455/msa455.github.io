# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 18:17:12 2021

@author: pmjum
"""

import markovify
import os.path
import json


def getHoroscopeModel():
    if(os.path.isfile("horoscopeModel.json")):
        #print("model already exists")
        with open("horoscopeModel.json", "r") as f:
            modelJson = json.load(f)
        horoscopeModel = markovify.Text.from_json(modelJson)
        return horoscopeModel
    else:
        #print("model does not yet exist")
        filename = "horoscopeTextRaw.txt"
        with open(filename, "r") as file:
            text = file.read()
            
        horoscopeModel = markovify.Text(text)
        modelJson = horoscopeModel.to_json()
        
        with open("horoscopeModel.json", "w") as jsonFile:
            json.dump(modelJson, jsonFile)
        
        return horoscopeModel
            

def generateRandomSentence(model,numSentences=1):
    text = ""
    for x in range(numSentences):
        text += model.make_sentence() + " "
    return text
 
def generateHoroscope(mainSign, model):
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    signs.remove(mainSign)
    text = ""
    for x in range(5):
        sentence = model.make_sentence()
        for sign in signs:
            if sign in sentence:
                sentence = sentence.replace(sign,mainSign)
        text += sentence + " "
    return text
        
    
print(generateHoroscope("Libra", getHoroscopeModel()))


