# coding=utf-8
"""
@author: 2cm
@software: pycharm
@file: main.py
@time: 2018/8/12 下午7:24
@desc:
"""
raw_corpus = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]


# Create a set of frequent words
stoplist = set('for a of the and to in'.split(' '))
# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in raw_corpus]

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

print (processed_corpus)
# processed_corpus

from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)

print(dictionary.token2id)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)

bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
print (bow_corpus)

from gensim import models
# train the model
tfidf = models.TfidfModel(bow_corpus)
# transform the "system minors" string
tfidf[dictionary.doc2bow("system minors".lower().split())]
# print (tfidf)


# text.collocations()
# from gensim.models.word2vec import Word2Vec
#
# profiler = Word2Vec()
#
# # word_source = [
# #     ['I', 'love', 'natural', 'language', 'processing'],
# #     ['word2vec', 'is', 'a', 'useful', 'model']
# # ]
#
# profiler.build_vocab(raw_corpus)
#
# profiler[raw_corpus]
#
#
# # print (profiler.similarity("woman", "man"))
# #
#
# profiler.train(raw_corpus)

