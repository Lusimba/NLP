import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt

#download the corpus
nltk.download('stopwords')
nltk.download('gutenberg')

stop_Words = set(stopwords.words('english'))

#read the corpus
words = nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt'))
#casefold the words
words = [word.lower() for word in words if word.isalpha()]
words = [word.lower() for word in words if word not in stop_Words]

fDist = FreqDist(words)

class my_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, WordList, Freq):
        self["Word"] = WordList
        self["Frequency"] = Freq

print("The total number of words is: {}".format(len(words))) #Total count
print("The Unique words are: {}".format(len(set(words)))) #Unique words

WordList = []
Freq = []
for x,v in fDist.most_common(10):
    WordList.append(str((x)))
    Freq.append(v)

table = my_dictionary()
table.add(WordList, Freq)
data = pd.DataFrame(table)
print (data)

Normfreq=[]
print("Normalized Outputs")
for x,v in fDist.most_common(10):
    Normfreq.append(v/len(fDist))

table.add(WordList, Normfreq)
Normalized = pd.DataFrame(table)
print(Normalized)


