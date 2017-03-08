import pickle
import model_generator
import bible_extract
import util

try:
    from nltk.translate import AlignedSent
    from nltk.translate import IBMModel2
except:
    from nltk.align import AlignedSent
    from nltk.align import IBMModel2

def train(book, iter1, iter2, use_ibm):
    if book != "wiki":
        regular_e = bible_extract.extract_verses_from_RE("RE_" + book)
        basic_e = bible_extract.extract_verses_from_BE("BE_" + book)
        e, f = util.linearize(regular_e, basic_e)
    else:
        xe = open("wiki.normal.aligned","rb").read().split('\n')
        xf = open("wiki.simple.aligned","rb").read().split('\n')
        e = []
        f = []
        for i in range(len(xe)):
            sxs = 0
            try:
                e.append(util.word_tokenize(xe[i].split('\t')[2].lower()))
                sxs = 1
                f.append(util.word_tokenize(xf[i].split('\t')[2].lower()))
            except:
                if sxs == 1:
                    e.pop()

    ve = util.get_vocab(e)
    vf = util.get_vocab(f)
    pickle.dump(vf, open("be-vocab.pk", "wb"))
    pickle.dump(ve, open("re-vocab.pk", "wb"))

    if not use_ibm:
        model_generator.generate_ibm1(e, f, ve, vf, "t-model1-" + str(iter1) + ".pk", iter1)
        t = pickle.load(open("t-model1-" + str(iter1) + ".pk","rb"))
        model_generator.generate_ibm2(t, e, f, ve, vf, "model2-" + str(iter2) + ".pk", iter2)
    else:
        bitext = []
        for i in range(len(e)/10):
            bitext.append(AlignedSent(f[i],e[i]))
        ibm2 = IBMModel2(bitext, iter2)

        try:
            t = util.to_t_dict(dict(ibm2.translation_table))
            a = util.to_a_dict(dict(ibm2.alignment_table))
        except:
            t = util.to_t_dict(dict(ibm2.probabilities))
            a = util.to_a_dict(dict(ibm2.alignments))

        pickle.dump(t, open("t-model2-" + str(iter2) + ".pk", "wb"))
        pickle.dump(a, open("a-model2-" + str(iter2) + ".pk", "wb"))
    
    t = pickle.load(open("t-model2-" + str(iter2) + ".pk","rb"))
    fast_tab = util.fast_table(t)
    pickle.dump(fast_tab, open("t-model2-" + str(iter2) + "-fast.pk","wb"))
    
