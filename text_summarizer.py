from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk
import heapq
import Sentence&Word_tokenizer as sw

url="https://en.wikipedia.org/wiki/Machine_learning"
allContent=""

htmlDoc=request.urlopen(url)

soupObject=bs(htmlDoc,'html.parser')
paraContents=soupObject.findAll('p')

for paraContent in paraContents:
    allContent+=paraContent.text
    
allContent_cleaned=re.sub(r'\[[0-9]*\]',' ',allContent)
finalContent=re.sub(r'\s+',' ',allContent_cleaned)

#Creating sentence token

sentence_tokens,words_tokens=sw.tokenizer(finalContent)

#calculate frequency

stopwords=nltk.corpus.stopwords.words('english')

word_frequencies = {}

for word in words_tokens:
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word]=1;
        else:
            word_frequencies[word]+=1

#calculate weighted frequency
max_frequency_word=max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word]=(word_frequencies[word]/max_frequency_word)

#calculate sentence score

sentence_scores={}

for sentence in sentence_tokens:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_frequencies.keys():
            if(len(sentence.split(' ')))<30:
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence]=word_frequencies[word]
                else:
                    sentence_scores[sentence]+=word_frequencies[word]

summary= heapq.nlargest(10,sentence_scores,key=sentence_scores.get)
print(summary)
