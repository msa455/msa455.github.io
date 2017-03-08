import pickle
import util
import bible_extract
import trainer
import translate
import random
import time
from gensim import corpora, models, similarities

# Load corpora
#########################################################
regular_e = bible_extract.extract_verses_from_RE("RE_Bible")
basic_e = bible_extract.extract_verses_from_BE("BE_Bible")
e, f = util.linearize(regular_e, basic_e)
#########################################################


# Train IBM Models
##########################################################
# trainer.train("Bible", 100, 100, True)
##########################################################


# Train Word2Vec Model
##########################################################
# sentences = e + f
# model = models.Word2Vec(sentences, size=100, window=5, min_count=1, workers=16)
# model.save("w2v-model.bin")
##########################################################


# Simplify text with Statistical Translation
##########################################################
# t = pickle.load(open("t-model2-100.pk","rb"))
# re_vocab_score = util.get_vocab_score(e)
# fast_t = pickle.load(open("t-model2-100-fast.pk","rb"))
# a = pickle.load(open("a-model2-100.pk","rb"))
# g = [[],[],[],[]]
# for i in range(len(e)):
#     g[0].append(translate.translate_sentence_ibm1_fast(fast_t, util.sentencify(e[i])))
#     g[1].append(translate.translate_sentence_ibm2_smart(fast_t, a, util.sentencify(e[i])))
# pickle.dump(g, open("g.pk","wb"))
##########################################################


# Calculate translation accuracy with Sentiment Analysis
##########################################################
# g = pickle.load(open("g.pk","rb"))
# model = models.Word2Vec.load("w2v-model.bin")
# combinations = [{"name":"ibm1-fast-vs-original","simple":g[0],"hard":e},
#                 {"name":"ibm2-fast-vs-original","simple":g[1],"hard":e},
#                 {"name":"ogden-vs-original","simple":f,"hard":e}]
# for c in combinations:
#     scores = []
#     for i in range(len(e)):
#         ss = [[],[]]
#         for word in c['simple'][i]:
#             if word in model.vocab:
#                 ss[0].append(word)
#         for word in c['hard'][i]:
#             if word in model.vocab:
#                 ss[1].append(word)
#         if len(ss[0]) != 0 and len(ss[1]) != 0:
#             score = model.n_similarity(ss[0], ss[1])
#             scores.append(score)
#     pickle.dump(scores, open(c['name'] + "-score.pk", "wb"))
##########################################################


# View accuracy scores
##########################################################
scores = [{"name":"ibm1-fast-vs-original"},
            {"name":"ibm2-fast-vs-original"},
            {"name":"ogden-vs-original"}]
for s in scores:
    score = pickle.load(open(s['name'] + "-score.pk", "rb"))
    print(s['name'] + ": " + str(sum(score)/len(score)))
##########################################################
