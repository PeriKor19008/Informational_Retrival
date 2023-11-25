import os
import nltk
from nltk.corpus import stopwords


class dictionary_maker:


    def __init__(self, path,filter):
        self.collectionPath = path
        self.filter = filter
        self.dict = []
        self.makeDictionary()




    def makeDictionary(self):
        if self.filter:
            stop_words = set(stopwords.words('english'))
        # Loop through all files in the directory
        for filename in os.listdir(self.collectionPath):
            # Construct the full path to the file
            file_path = os.path.join(self.collectionPath, filename)

            # Check if the item is a file (not a subdirectory)
            if os.path.isfile(file_path):
                # Open and read the file
                with open(file_path, 'r') as file:
                    # Read and print each line/word
                    word_index = 0
                    for word in file:
                        word = word.rstrip('\n')

                        if self.filter:
                            if not word.lower() in stop_words:
                                self.add_word_to_dict(word,filename,word_index)
                        else:
                            self.add_word_to_dict(word,filename,word_index)
                        word_index = word_index + 1



    def add_word_to_dict(self,word,filename,word_index):
        # dictionary is order by #ocurance (dict[1])
        # so common words will be in the top making searching faster

        # search_for_word returns -1 if word doesn't exist in dictionary
        index=self.search_for_word(word)
        if index < 0:
            occurrence = [filename,[word_index]]
            line = [word, 1,[occurrence]]
            self.dict.append(line)
        else:


            # search if filename is in line (self.dict[index])
            exist = False
            for occ in self.dict[index] [2]:
                if occ[0]==filename:
                    occ[1].append(word_index)
                    self.correct_indexes(index)
                    exist = True
                    return
            if not exist:
                self.dict[index][1] = self.dict[index][1] + 1
                occ = [filename,[word_index]]
                self.dict[index][2].append(occ)

    def correct_indexes(self,index):
        if index == 0:
            return
        while(True):
            if self.dict[index][1] > self.dict [index - 1][1]:
                self.dict[index], self.dict[index - 1] = self.dict[index - 1], self.dict[index]
            else:
                return
    def search_for_word(self,word):
        i = 0
        for line in self.dict:
            if line[0]==word:
                return i
            i = i +1
        i = -1
        return i



        