# -*- coding: utf-8 -*-

#Import gensim for semantic comparisons and nltk for text processing
from gensim import corpora, models, similarities
from nltk import tokenize as tk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
###------------PRE-PROCESSING------------------###
#Specify which files to work with
#THIS SHOULD BE THE ONLY PART OF CODE TO CHANGE WITH EACH USE
simpleFile = "texts/psalm23Simple.txt"
hardFile = "texts/psalm23Hard.txt"

#Open the simple and difficult files to compare
print("opening files and extracting information...")
with open(simpleFile, "r") as simple, open(hardFile, "r") as hard:
    simpleText = simple.read()
    hardText = hard.read()
simple.close()
hard.close()

#remove numbers from the text BEFORE preprocessing with nltk
print("preprocessing information...")
def removeNum(string):
    temp = ""
    for char in string:
        if(char.isdigit()==False):
            temp += char
    return(temp)

simpleText = removeNum(simpleText)
hardText = removeNum(hardText)

#separate the texts into sentences
print("tokenizing information...")
simpleSentTokens = tk.sent_tokenize(simpleText)
hardSentTokens = tk.sent_tokenize(hardText)

#tokenize the sentences into individual words, ignoring punctuation
tkz = tk.RegexpTokenizer(r'\w+')

simpleTokens = []
for sent in simpleSentTokens:
    simpleTokens.append(tkz.tokenize(sent))
    
hardTokens = []
for sent in hardSentTokens:
    hardTokens.append(tkz.tokenize(sent))
#print(hardTokens)

#remove stopwords from the tokens and stem them
lmtzr = WordNetLemmatizer()
def removeStops(string):
    temp = []
    for sentence in string:
        temp2 = []
        for word in sentence:
            word = lmtzr.lemmatize(word.lower())
            if word not in stopwords.words("english"):
                temp2.append(word)
        temp.append(temp2)
    return(temp)

simpleTokens = removeStops(simpleTokens)
hardTokens = removeStops(hardTokens)
print("preprocessing complete")
#print(simpleTokens)
print(len(simpleTokens))
#print(hardTokens)
print(len(hardTokens))
###----------SEMANTIC SIMILARITY COMPARISON-----------###

#load the pretrained model
print("loading pretrained word2vec model...")
model = models.Word2Vec.load_word2vec_format("pretrainedVecs.bin.gz", binary=True)

scores = []
for x in range(len(simpleTokens)):
    temp1 = []
    temp2 = []
    for word in simpleTokens[x]:
        if word in model.vocab:
            temp1.append(word)
    for word in hardTokens[x]:
        if word in model.vocab:
            temp2.append(word)
    print(temp1)
    print(temp2)
    score = model.n_similarity(temp1,temp2)
    scores.append(score)
    print(score)
    
print("comparison complete")
print(scores)
