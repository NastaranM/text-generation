#!/usr/bin/env python3

import sys
import os
import text_stats
import random
import re
from collections import Counter
from collections import namedtuple
from collections import defaultdict

""" This code uses the text_stats.py file to create a new text 
based on the statistics provided by text_stats.py"""

"""The words are selected based on the most repeated words after the input word by the user.
The next word is selected based on the weighted average of the repitition.
Each next word is selected by considering the most repeated word and randomly selected 
based on their probability of occurance."""

def main(filename,starting_word,max_num_words):
    data_base= text_stats.database(filename)[0]
    words = [x for x in re.split("\W",data_base) if x]
    allWordCount= Counter(tuple(words[i:i+2]) for i in range(len(words)-1))
    word =namedtuple("word",["frstword","nxtword","freq"])
    wordDatabase = []
    for wrd, frq in allWordCount.items():
        wordDatabase.append(list(word._make([wrd[0],wrd[1],frq])))
    wordRepository = defaultdict(list)
    for wrd,nxtwrd,frq in wordDatabase:
        wordRepository[wrd].append([nxtwrd,frq])
    cur_word = str(starting_word)
    msg=cur_word + " "
    while max_num_words>1:
        for word,cnt in wordRepository.items():
            if cur_word == word:
                weights = []
                wordlist = []
                for i in range(len(cnt)):
                    weights.append(cnt[i][1])
                    wordlist.append(cnt[i][0])
        selected = random.choices(wordlist,weights)
        msg +=  cur_word + " "
        cur_word = str(selected[0])
        max_num_words-=1
    print(msg)

if __name__ == "__main__":
    if  len(sys.argv)<4:
        print("ERROR")
    else:
        print("This is the name of the script {}".format(sys.argv[0]))
        filename = sys.argv[1]
        starting_word = str(sys.argv[2])
        max_num_words = int(sys.argv[3])
        if isinstance(max_num_words,int) == False:
            print("ERROR: Please enter an integer for the last argument")
        else:
            if os.path.isfile(sys.argv[1]):
                print("The second argument is ", filename)
                print("The number of arguments is ", len(sys.argv))
                print("The argumnents are ", str(sys.argv))
                main(filename,starting_word,max_num_words)
            else:
                print("ERROR: File not in path")
    

         
         
         
         
    
