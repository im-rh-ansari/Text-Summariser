from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk
import heapq
import Sentence&Word_tokenizer as sw
import Score_calculator as sc

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

sentence_scores=sc.score(sentence_tokens,word_frequencies)

summary= heapq.nlargest(10,sentence_scores,key=sentence_scores.get)
print(summary)
