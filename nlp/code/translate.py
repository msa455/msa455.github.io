import pickle
import util

def translate_sentence_ibm2_smart(fast_table, q, sentence):
    ee = util.word_tokenize(sentence.lower())
    best_ff = []
    best_p = 0
    l = len(ee)
    js = list(range(1,l+1))

    for m in range(l-1,l+1):
        sentence_p = 0
        ff = []
        for i in range(1,m+1):
            max_p = 0
            F = ""
            best_j = 0
            for j in js:
                E = ee[j-1]
                W = fast_table.get(E,"")
                try:
                    p = q[j][i][l][m] * fast_table[E + "<=>" + W]
                except:
                    p = 0
                if p > max_p:
                    max_p = p
                    F = W
                    best_j = j
            
            if F != "":
                ff.append(F)
                js.remove(best_j)
            sentence_p += max_p

        if sentence_p > best_p:
            best_p = sentence_p
            best_ff = list(ff)

    return best_ff

def translate_sentence_ibm1_fast(fast_table, sentence):
    ee = util.word_tokenize(sentence.lower())
    ff = []
    for E in ee:
        F = fast_table.get(E, '')
        ff.append(F)
    
    return ff

def translate_sentence_ibm1_standard(t, re_vocab_score, sentence):
    ee = util.word_tokenize(sentence.lower())
    ff = []
    for E in ee:
        max_score = 0
        F = ''
        for f in t[E]:
            score = t[E][f] * re_vocab_score[f]
            if score > max_score:
                max_score = score
                F = f
        ff.append(F)
    
    return ff