# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:08:06 2017

@author: Main Character
"""

import json
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import bigrams
import string
import vincent

tweets = []
terms = []
hashes = []
calls = []
   
cur_search = "#love"

dead = ['rt','via','…','RT','❤','amp',' ', '']
punc = list(string.punctuation)
stop = (stopwords.words("english") + punc + dead)  
stops = set(stop)
emoticons_str = r"""
    (?:
    [:=;] # Eye
    [oO\-]? # Nose (optional)
    [D\)\]\(\]/\\OpP] # Mouth
     )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
    
def preprocess(s, lowercase=False):
    tokens=tokens_re.findall(s)
    if(lowercase):
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return(tokens)
    
lmtzr = WordNetLemmatizer()
def removeStops(string):
    temp = []
    for sentence in string:
        temp2 = []
        for word in sentence:
            #word = lmtzr.lemmatize(word.lower())
            if word not in stopwords.words("english"):
                temp2.append(word)
        temp.append(temp2)
    return(temp)
    
with open('tweets2.json', 'r') as f:
    #to process the first tweet
    #line = f.readline()
    #tweet = json.loads(line)
    #print(word_tokenize(tweet['text']))
    ##to process the entire file
    for line in f:
        try:
            tweet = json.loads(line)
            #tokens = removeStops(tweet['text'])
            tokens = preprocess(tweet['text'])
            for term in tokens:
                term = term.lower()
                if term!=cur_search and term not in stops and term.isdigit() == False:
                    if term.startswith("#"):
                        hashes.append(term)
                    #elif term.startswith("@"):
                    #    calls.append(term)
                    else:
                        terms.append(term)
            tweets.append(tokens)
        except Exception:
            pass
    f.close()
    
term_counter = Counter()
term_counter.update(terms)
term_freq = term_counter.most_common(10)

print("Most common terms: " + str(term_freq))
hash_counter = Counter()
hash_counter.update(hashes)
print("Most common hashtags: " + str(hash_counter.most_common(10)))

labels,freq = zip(*term_freq)
data = {'data':freq,'x':labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')

#call_counter = Counter()
#call_counter.update(calls)
#print("Most common usercalls: " + str(count_all.most_common(10)))   

 

    
    
