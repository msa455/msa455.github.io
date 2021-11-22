# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 01:02:40 2021

@author: sam
"""

import jaconv

def createGibberishWord(word, languageSyllables, hiragana_chart, katakana_chart, hir2kat):
    kana = jaconv.alphabet2kana(word)
    kana = list(kana)
    temp = []
    word = ""
    #I remove duplicate characters because kanas often get duplicated and lead to a lot of double vowels
    lastChar = ""
    for char in kana:
        if char in hiragana_chart:
            char = char.translate(hir2kat)
        if(char != lastChar):
            temp.append(char)
        lastChar = char
    for char in temp:
        #word += languageSyllables[katakana_num_dict[char] % len(languageSyllables)]
        word += languageSyllables[katakana_chart.index(char) % len(languageSyllables)]

        word+="-"
    return(word.rstrip("-"))
    
def gibberish_post(text,language, allSyllables, hiragana_chart, katakana_chart, hir2kat):
    #get the text and the language of choice from the user form
    text = text.lower()
    languageVals = {"elvish":0,"goblin":1}
    syllables = allSyllables[languageVals[language]]

    #convert the text into some approximation of katakana.
    #this doesnt need to be an accurate translation, just a method for some form of syllables
    gibberish = "" 
    for word in text.split():
        gibberish += createGibberishWord(word,syllables,hiragana_chart,katakana_chart, hir2kat)
        gibberish += " "
    return(gibberish.rstrip(" "))