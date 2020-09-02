"""
Created on Sat Aug 29 16:13:12 2020

@author: harshitha palvai
"""

import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
  
# Input text - to summarize  
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from googletrans import Translator  #used to translate telugu to english and vice versa
translator = Translator()

#opening a file and reading into other variable
with open('telugu.txt', 'r',encoding="utf8") as myfile: 
    t1=myfile.read().replace('\n', '') #updating into a string
print(t1)#printing string


t=translator.translate(t1) #translating into english
print()
text= t.text


#print(text) 
# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 


# Creating a frequency table to keep the  
# score of each word 
   
freqTable = dict() 
for word in words: 
    word = word.lower() 
    if word in stopWords: 
        continue
    if word in freqTable: 
        freqTable[word] += 1
    else: 
        freqTable[word] = 1
   
# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 
   
for sentence in sentences: 
    for word, freq in freqTable.items(): 
        if word in sentence.lower(): 
            if sentence in sentenceValue: 
                sentenceValue[sentence] += freq 
            else: 
                sentenceValue[sentence] = freq 
   
   
   
sumValues = 0
for sentence in sentenceValue: 
    sumValues += sentenceValue[sentence] 
   
# Average value of a sentence from the original text 
   
average = int(sumValues / len(sentenceValue)) 
   
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 

print()
print()
#print(summary) 
#translating it into english
s=translator.translate(src='en',dest='te',text=summary)
print("SUMMARISED TEXT:\n")
print(s.text)