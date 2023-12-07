import math

import main
def makeVector(dictionary,tf_calculation_type,idf_calculation_type):
    DocVectors = []
    for term in dictionary:
        for occurance in term[2]:
            tf = len(occurance[1])/term[1]
            if tf_calculation_type == 1:
                tf = 1 + math.log(tf)
            if
            index = getDocIndex(DocVectors,occurance[0])
            if index == -1:



def getDocIndex(DocVector, doc):
    i =0
    for vector in DocVector:
        if vector[0] == doc:
            return i
        i = i + 1
    return -1