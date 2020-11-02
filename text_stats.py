#!/usr/bin/env python3


# how to run: python readings_01.py shakespeare.txt "king" 3
"""
Created on Sun Mar 29 19:24:27 2020

@author: Nastaran Meftahi
"""
import os
import sys
from collections import Counter
import re
from collections import OrderedDict

"""In this section I created a database to read the file from the shakespeare.txt.
The file gets clean and two sets of results with the sorted and unsorted words are returned.
"""
    
def database(filename):
    with open (filename,encoding='utf-8') as txt:
            lines = txt.read()
            lines = re.sub('[^a-zA-Z ]+', '', lines)
            lines = re.sub("\s\s+" , " ", lines)
            st = "START OF THIS PROJECT GUTENBERG EBOOK THE COMPLETE WORKS OF WILLIAM SHAKESPEARE"
            a = lines.index("".join(st[0:len(st)]))
            b = a+len(st)
            nd = " FINIS"
            c= lines.index("".join(nd[0:len(nd)]))
            d = c + len(nd)
            res = lines[b:d]
            unsortedwords = res.lower()
            sortedword = sorting(unsortedwords)
    return unsortedwords, sortedword


"""The 5 most common words from the database is retrieved."""

def mostcom5(allwords):
    mostcom = dict(Counter(allwords).most_common(5))
    mostcom5 = OrderedDict((k, v) for k, v in sorted(mostcom.items(), key=lambda x: x[0]))
    return mostcom5 

# A list of unique words are retrieved

def uniqword(allwords):    
    unique_words = {}
    for word, count in allwords.items():
        if count == 1:
            unique_words[word] = count
    return unique_words
    

# The sequence of words following a specific word determined by the user is retrieved.

def word_seq(unsortedwords,target,n):
    word = target
    s="\s"
    matching = "(?:[^a-zA-Z'-]+[a-zA-Z'-]+)"
    r1 = re.findall(s+word+matching, unsortedwords)
    b = [i.split()[1:2] for i in r1]
    d = dict(Counter(tuple(item) for item in b))
    final = OrderedDict((k[0], v) for k, v in sorted(d.items(), key=lambda x: x[0]))
    final = dict(Counter(final).most_common(n))
    return final

# A sorting function for unsorted words
def sorting(unsortedwords): 
    word = unsortedwords.split(" ") 
    word.sort() 
    sortedword = " ".join(word) 
    return sortedword

# Counting the number of alphabets in each word.
def alphacount(sortedword):
    alphabet_count = {}
    for word in sortedword:
        for letter in word:
            keys = alphabet_count.keys()
            if letter in keys:
                alphabet_count[letter]+=1
            else:
                alphabet_count[letter] =1
    alphabet_count.pop(' ')
    alphabets = OrderedDict((k, v) for k, v in sorted(alphabet_count.items(), key=lambda item: item[1],reverse = True))
    return alphabets 
    
""" A function which gets an input file name and file directory for providing 
the statistics of the words in a text-based dataset. 
These statistics include:
                        the most commong words,
                        word count of the text,
                        word sequence,
                        The number of unique words,
                        The number of words in the text without counting their repitition.
""" 

def presentation(filename,newfile = None):
    unsortedwords, sortedword = database(filename)
    #unsortedwords =  database(filename)[0]
    allwords = dict(Counter(sortedword.split()))
    alphabets = alphacount(sortedword)
    unique_words = uniqword(allwords)
    unique_words_count = len(unique_words)
    word_counter = len(allwords)
    tot_words = sum(allwords.values())
    #wordseq = word_seq(unsortedwords,str(target),n)
    most_common = mostcom5(allwords)
    if newfile == None:
        for word, count in alphabets.items():
            print(word, ' : ', count,"\n")
        print("---\n")
        print("Five most commong words are \n")
        for word,count in most_common.items():
            print(word, ' : ', count,"\n") 
            #print("\n")
            wordseq = word_seq(unsortedwords,str(word),3)
            for  word, count in wordseq.items():
                print("   ",word, ' : ', count, "\n")
            print("---\n")
        #print("---\n")
        print("The number of  words without repititions: {} \n".format(word_counter))
        print("---\n")
        print("Total number of words: {} \n".format(tot_words))
        print("---\n")
        print("Number of unique words  : {} \n".format(unique_words_count))
        print("---\n")
    else:
        with open("{}.txt".format(newfile), "w") as f:
        #f = open("{}.txt".format(newfile), "w")
            for word, count in alphabets.items():
                f.write("{}:{}\n".format(word,count))
            f.write("---\n")
            f.write("Five most commong words are \n")
            for word,count in most_common.items():
                f.write("{}:{}\n".format(word,count)) 
                #print("\n")
                wordseq = word_seq(unsortedwords,str(word),3)
                for  word, count in wordseq.items():
                    f.write("\t{}:{}\n".format(word,count))
                f.write("---\n")
            f.write("The number of  words without repititions: {} \n".format(word_counter))
            f.write("---\n")
            f.write("Total number of words: {} \n".format(tot_words))
            f.write("---\n")
            f.write("Number of unique words  : {} \n".format(unique_words_count))
            f.write("---\n")
        #f.close()
        
 

def main(*argv):
    if len(argv) >= 3:
        presentation(filename,newfile)
    else:
        presentation(filename,newfile = None)  

    
if __name__ == "__main__":
    if  len(sys.argv)<2:
        print("ERROR")
    elif len(sys.argv)==2:
        print("This is the name of the script {}".format(sys.argv[0]))
        filename = sys.argv[1]
        if os.path.isfile(sys.argv[1]):
            print("The second argument is ", filename)
            print("The number of arguments is ", len(sys.argv))
            print("The argumnents are ", str(sys.argv))
            main(*sys.argv)
        else:
            print("ERROR: File not in path")
    elif len(sys.argv)==3:
        print("This is the name of the script {}".format(sys.argv[0]))
        filename = sys.argv[1]
        newfile = sys.argv[2]
        if os.path.isfile(sys.argv[1]):
            print("The second argument is ", filename)
            print("The new file is written in ",newfile)
            print("The number of arguments is ", len(sys.argv))
            print("The argumnents are ", str(sys.argv))
            main(*sys.argv)
    else:
        print("ERROR: too many argument")
        


# Questions
        
"""In what way did you "clean up" or divide up the text into words (in the 
program; the text files should be left unaffected)? """

"""The cleaning step has been done by eliminating all characters except for al
-phabetical (capital/small) and space. Then we removed multiple spaces. Then
we removed anything before 'START OF THIS PROJECT GUTENBERG EBOOK THE COMPLETE 
WORKS OF WILLIAM SHAKESPEARE' and after 'FINIS'. In the next step we convert 
everything to small alphabets."""

""" Which data structures have you used (such as lists, tuples, dictionaries, 
sets, ...)? Why does that choice make sense?"""

"""We used arrays(string datatype), lists, dictionaries and tuples. We needed
to have two types of data in the memory without having a long runtime. So, we 
created a database function which provides us with two pieces of results, an 
array of the cleaned up text, a sorted list of the cleaned up text. We need 
these two variables, because every results we get should be sorted and sorting
is an expensive task. It is better to produce it only once and extract from
it. We also need the original clean text as we need to find the sequence of 
words and their frequencies.
We are representing everything in a dictionary format, so dictionary is a
useful data structure. However,nested lists do not work well with the package
Counter that we used. So we used tuples to convert the word sequence in dictionary format."""