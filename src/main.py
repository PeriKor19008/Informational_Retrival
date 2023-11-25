from inverted_dictionary import dictionary_maker
if __name__ == '__main__':
    # if second arg on dictionary_maker is 1 stop words (and,or etc) will be filtered out
    # if it is 0 then they will not
    D = dictionary_maker("docs",1)
    dict = D.dict
