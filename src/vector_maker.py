import math

import numpy as np


def Vectrorize(doc,dictionary,tf_calculation_type,idf_calculation_type):
    docVector = []
    for term in dictionary:
        for occ in term[2]:
            docVector.append(0)
            if int(occ[0]) == doc:
                tf = len(occ[1]) / term[1]
                if tf_calculation_type == 1:
                    tf = 1 + math.log(tf)
                idf = len(dictionary) / term[1]
                if idf_calculation_type == 0:
                    idf = math.log(idf, 10)
                else:
                    idf = math.log(idf + 1, 10)
                value = idf * tf
                docVector[-1] = value
                break
    return docVector

def VectorizeQuery(query,dictionary,tf_calculation_type,idf_calculation_type):
    docVector = []
    words = query.split()
    word_frequency = {}
    for word in words:
        word = word.upper()
        # If the word is already in the dictionary, increment its count; otherwise, set its count to 1.
        word_frequency[word] = word_frequency.get(word, 0) + 1
    for term in dictionary:
        if term[0] in word_frequency:
            tf = word_frequency[word] / len(words)
            if tf_calculation_type == 1:
                tf = 1 + math.log(tf)
            idf = idf = len(dictionary) / term[1]
            if idf_calculation_type == 0:
                idf = math.log(idf, 10)
            else:
                idf = math.log(idf + 1, 10)
            value = tf * idf
            docVector.append(value)
        else:
            docVector.append(0)
    return docVector


def makeDocVectors(dictionary,doc_num,tf_calculation_type,idf_calculation_type):
    DocVector = []
    for doc in range(doc_num):
        vector = Vectrorize(doc,dictionary,tf_calculation_type,idf_calculation_type)
        DocVector.append(vector)

def cosine_similarity(a,b):
    similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return similarity