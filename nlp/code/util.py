import pickle
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

def dezerofy(t):
    for k in list(t):
        for v in list(t[k]):
            if t[k][v] == 0:
                t[k].pop(v)
    return t

def fast_table(t):
    tab = dict()
    for k in t:
        p = 0
        w = 'NULL'
        for v in t[k]:
            if t[k][v] > p:
                p = t[k][v]
                w = v
        tab[str(k)] = str(w)
        tab[str(k) + "<=>" + str(w)] = p
    return tab

def sentencify(ff):
    if len(ff) <= 1:
        return "???"
    
    try:
        ff[0] = ff[0][0].upper() + ff[0][1:]
    except:
        pass
    
    res = " ".join(ff)
    for i in range(len(res)-1):
        try:
            if res[i] == " " and res[i+1] in ".,?!:":
                res = res[:i] + "`" + res[i+1:]
            elif res[i] in ".?!" and res[i+1] == " ":
                res = res[:i+2] + res[i+2].upper() + res[i+3:]
        except:
            pass
    res = res.replace("`","")
    return res

def get_vocab(l):
    vocab = []
    for s in l:
        for w in s:
            vocab.append(w)
    return set(vocab)

def get_vocab_score(l):
    vocab = []
    for s in l:
        for w in s:
            vocab.append(w)
    score = {}
    for w in vocab:
        score[w] = vocab.count(w) / len(vocab)
    return score

def get_word_freq(l):
    f = dict()
    for s in l:
        for w in s:
            if w in f:
                f[w] += 1
            else:
                f[w] = 1
    for w in f:
        f[w] /= len(f)
    return f

def initialize_t(a, b):
    x = {}
    for k in a:
        if k not in x:
            x[k] = {}
        for kk in b:
            x[k][kk] = 1 / (len(b))
    return x

def initialize_a(a, b):
    x = {}
    for i in range(len(a)):
        ee = a[i]
        ff = b[i]
        l_e = len(ee)
        l_f = len(ff)
        for (k, F) in enumerate(ff, 1):
            if k not in x:
                x[k] = {}
            for (j, E) in enumerate(ee, 1):
                if j not in x[k]:
                    x[k][j] = {}
                if l_e not in x[k][j]:
                    x[k][j][l_e] = {}
                x[k][j][l_e][l_f] = 1 / (l_f + 1)
    return x

def initialize_quatro(a, b):
    x = {}
    for i in range(len(a)):
        ee = a[i]
        ff = b[i]
        l_e = len(ee)
        l_f = len(ff)
        for (k, F) in enumerate(ff, 1):
            if k not in x:
                x[k] = {}
            for (j, E) in enumerate(ee, 1):
                if j not in x[k]:
                    x[k][j] = {}
                if l_e not in x[k][j]:
                    x[k][j][l_e] = {}
                x[k][j][l_e][l_f] = 0
    return x

def initialize_trio(a, b):
    x = {}
    for i in range(len(a)):
        ee = a[i]
        ff = b[i]
        l_e = len(ee)
        l_f = len(ff)
        for (j, E) in enumerate(ee, 1):
            if j not in x:
                x[j] = {}
            if l_e not in x[j]:
                x[j][l_e] = {}
            x[j][l_e][l_f] = 0
    return x


def initialize_matrix(a, b):
    x = {}
    for k in a:
        if k not in x:
            x[k] = {}
        for kk in b:
            x[k][kk] = 0
    return x

def initialize_list(a):
    x = {}
    for k in a:
        x[k] = 0
    return x

def word_tokenize(sentence):
    for ch in ".,!?:;/()-":
        sentence = sentence.replace(ch, " " + ch + " ")
    words = sentence.split()
    return words

def linearize_chapter(rege, base):
    e = []
    f = []
    for k in rege:
        if k in base:
            for kk in rege[k]:
                if kk in base[k]:
                    s1 = word_tokenize(rege[k][kk].lower())
                    s2 = word_tokenize(base[k][kk].lower())
                    e.append(s1)
                    f.append(s2)
    return e,f

def linearize(rege, base):
    chapters = pickle.load(open("chapters.pk","rb"))
    e = []
    f = []
    for chap in chapters:
        for k1 in rege[chap]:
            for k2 in rege[chap][k1]:
                try:
                    s1 = word_tokenize(rege[chap][k1][k2].lower())
                    s2 = word_tokenize(base[chap][k1][k2].lower())
                    e.append(s1)
                    f.append(s2)
                except:
                    pass
    return e,f

def to_t_dict(ft):
    t = dict()
    for w1 in ft:
        if w1:
            t[w1] = dict()
            for w2 in ft[w1]:
                if w2:
                    t[w1][w2] = ft[w1][w2] 
    return t

def to_a_dict(fa):
    a = dict()
    for k in fa:
        if k:
            a[k] = dict()
            for l in fa[k]:
                if l:
                    a[k][l] = dict()
                    for m in fa[k][l]:
                        if m:
                            a[k][l][m] = dict()
                            for n in fa[k][l][m]:
                                a[k][l][m][n] = fa[k][l][m][n] 
    return a


def removeStops(string):
    lmtzr = WordNetLemmatizer()
    temp = []
    for sentence in string:
        temp2 = []
        for word in sentence:
            word = lmtzr.lemmatize(word.lower())
            if word not in stopwords.words("english"):
                temp2.append(word)
        temp.append(temp2)
    return temp